import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    w = lines[1]
    s = lines[2]

    open_to_close = {"(": ")", "[": "]"}
    close_to_open = {")": "(", "]": "["}

    stack = []
    for char in s:
        if char in open_to_close:
            stack.append(char)
        elif stack and stack[-1] == close_to_open[char]:
            stack.pop()

    tail = []
    remain = n - len(s)
    while remain:
        if remain == len(stack):
            char = stack.pop()
            tail.append(open_to_close[char])
            remain -= 1
        else:
            for candidate in w:
                if candidate in open_to_close:
                    tail.append(candidate)
                    stack.append(candidate)
                    remain -= 1
                elif stack and candidate == open_to_close[stack[-1]]:
                    tail.append(candidate)
                    stack.pop()
                    remain -= 1
                else:
                    continue
                break

    return s + "".join(tail)


if __name__ == "__main__":
    result = main()
    print(result)
