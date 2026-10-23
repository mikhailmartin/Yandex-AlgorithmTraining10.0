import sys
from dataclasses import dataclass
from enum import Enum
from itertools import chain


# LAB - Left Angle Bracket
# RAB - Right Angle Bracket
LAB = "<"
RAB = ">"
SLASH = "/"


class TagType(Enum):
    OPEN = 0
    CLOSE = 1


@dataclass
class Tag:
    tag_type: TagType
    tag_name: str

    def __repr__(self) -> str:
        return f"<{SLASH if self.tag_type == TagType.CLOSE else ''}{self.tag_name}>"


class XmlValidationError(Exception):
    ...


class XmlSyntaxError(XmlValidationError):
    def __init__(self, pos: int) -> None:
        self.pos = pos


class NoLabError(XmlSyntaxError):
    ...


class ImpossibleLabError(XmlSyntaxError):
    ...


class RabWithEmptyContentError(XmlSyntaxError):
    ...


class UnexpectedLabError(XmlSyntaxError):
    ...


class UnexpectedSlashError(XmlSyntaxError):
    ...


class NoRabError(XmlSyntaxError):
    ...


class XmlStructureError(XmlValidationError):
    ...


class ExtraCloseError(XmlStructureError):
    def __init__(self, idx: int) -> None:
        self.idx = idx


class MissMatchError(XmlStructureError):
    def __init__(self, open_idx: int, close_idx: int) -> None:
        self.open_idx = open_idx
        self.close_idx = close_idx


class UnclosedError(XmlStructureError):
    def __init__(self, stack: list[int]) -> None:
        self.stack = stack


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    string = lines[0]

    string = list(string)
    letters = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    techs = ["<", ">", "/"]

    try:
        tags = parse_tags(string)

        try:
            is_valid_xml(tags)
        except ExtraCloseError as e:
            # кажется, это возможно только если тэг стал по ошибке закрывающим
            for char in letters:
                origin_tag = tags[e.idx]
                tags[e.idx] = Tag(TagType.OPEN, char + tags[e.idx].tag_name)
                try:
                    if is_valid_xml(tags):
                        return "".join([str(tag) for tag in tags])
                except XmlValidationError:
                    tags[e.idx] = origin_tag
        except MissMatchError as e:

            def try_replace_tag(idx: int, new_tag: Tag):
                old_tag = tags[idx]
                tags[idx] = new_tag
                try:
                    if is_valid_xml(tags):
                        return "".join(str(tag) for tag in tags)
                except XmlValidationError:
                    pass
                tags[idx] = old_tag
                return None

            # Вариант: открывающий тег на самом деле был закрывающим.
            # Например, <wit> должно было быть </it>.
            open_tag = tags[e.open_idx]
            if len(open_tag.tag_name) > 1:
                result = try_replace_tag(
                    e.open_idx,
                    Tag(TagType.CLOSE, open_tag.tag_name[1:])
                )
                if result is not None:
                    return result

            # Вариант: закрывающий тег на самом деле был открывающим.
            # Например, </c> могло быть <bc>.
            close_tag = tags[e.close_idx]
            for char in letters:
                result = try_replace_tag(
                    e.close_idx,
                    Tag(TagType.OPEN, char + close_tag.tag_name)
                )
                if result is not None:
                    return result

            # Уже после этого можно безопасно пробовать замену буквы в имени,
            # но только если длины имён совпадают.
            open_tag = tags[e.open_idx]
            close_tag = tags[e.close_idx]

            if len(open_tag.tag_name) == len(close_tag.tag_name):
                diffs = [
                    i for i in range(len(open_tag.tag_name))
                    if open_tag.tag_name[i] != close_tag.tag_name[i]
                ]

                if len(diffs) == 1:
                    i = diffs[0]

                    result = try_replace_tag(
                        e.open_idx,
                        Tag(
                            open_tag.tag_type,
                            open_tag.tag_name[:i]
                            + close_tag.tag_name[i]
                            + open_tag.tag_name[i + 1:]
                        )
                    )
                    if result is not None:
                        return result

                    result = try_replace_tag(
                        e.close_idx,
                        Tag(
                            close_tag.tag_type,
                            close_tag.tag_name[:i]
                            + open_tag.tag_name[i]
                            + close_tag.tag_name[i + 1:]
                        )
                    )
                    if result is not None:
                        return result
        except UnclosedError as e:
            for idx in e.stack:
                if tags[idx].tag_name[1:] == "":
                    continue
                origin_tag = tags[idx]
                tags[idx] = Tag(TagType.CLOSE, tags[idx].tag_name[1:])
                try:
                    if is_valid_xml(tags):
                        return "".join([str(tag) for tag in tags])
                except XmlValidationError:
                    tags[idx] = origin_tag

    except NoLabError as e:
        for pos in (e.pos, e.pos - 1):
            if not (0 <= pos < len(string)):
                continue

            for char in chain(techs, letters):
                if char == string[pos]:
                    continue

                new_string = replace(string, pos, char)

                try:
                    tags = parse_tags(new_string)
                    if is_valid_xml(tags):
                        return "".join(new_string)
                except XmlValidationError:
                    pass

        return "".join(string)
    except (ImpossibleLabError, UnexpectedSlashError) as e:
        for char in chain(techs, letters):
            new_string = replace(string, e.pos, char)
            try:
                tags = parse_tags(new_string)
                if is_valid_xml(tags):
                    return "".join(new_string)
            except XmlValidationError:
                pass
    except (RabWithEmptyContentError, UnexpectedLabError) as e:
        for i in (e.pos - 1, e.pos):
            for char in chain(techs, letters):
                new_string = replace(string, i, char)
                try:
                    tags = parse_tags(new_string)
                    if is_valid_xml(tags):
                        return "".join(new_string)
                except XmlValidationError:
                    pass
    except NoRabError as e:
        string[e.pos] = RAB
        return "".join(string)

    return "".join(string)


def parse_tags(string: list[str]) -> list[Tag]:

    n = len(string)

    tags = []
    i = 0
    while i < n:
        tag_name = []

        # первый символ
        if string[i] != LAB:
            raise NoLabError(i)
        i += 1

        # второй символ
        if i >= n:
            raise NoRabError(i - 1)
        char = string[i]
        if char == LAB:
            raise ImpossibleLabError(i)
        elif char == RAB:
            raise RabWithEmptyContentError(i)
        elif char == SLASH:
            tag_type = TagType.CLOSE
        else:
            tag_type = TagType.OPEN
            tag_name.append(char)
        i += 1

        # в ожидании последнего
        tag_ready = False
        while i < n and not tag_ready:
            char = string[i]
            if char == LAB:
                raise UnexpectedLabError(i)
            elif char == SLASH:
                raise UnexpectedSlashError(i)
            elif char == RAB:
                if not tag_name:
                    raise RabWithEmptyContentError(i)
                tag_name = "".join(tag_name)
                tag = Tag(tag_type, tag_name)
                tags.append(tag)
                tag_ready = True
            else:
                tag_name.append(char)
            i += 1

    if isinstance(tag_name, list):
        raise NoRabError(i-1)

    return tags


def replace(string: list[str], i: int, char: str) -> list[str]:
    new_string = string.copy()
    new_string[i] = char
    return new_string


def is_valid_xml(tags: list[Tag]) -> bool:

    stack = []
    for idx, tag in enumerate(tags):
        if tag.tag_type == TagType.OPEN:
            stack.append(idx)
        elif tag.tag_type == TagType.CLOSE:
            if not stack:
                raise ExtraCloseError(idx)
            if tags[stack[-1]].tag_name == tag.tag_name:
                stack.pop()
            else:
                raise MissMatchError(stack[-1], idx)

    if stack:
        raise UnclosedError(stack)

    return True


if __name__ == "__main__":
    result = main()
    print(result)
