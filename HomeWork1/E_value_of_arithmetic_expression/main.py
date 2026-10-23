import sys


def main(lines: list[str] | None = None) -> str | int:

    lines = lines or sys.stdin.read().splitlines()

    string = lines[0]

    infix = to_infix(string)
    try:
        validate(infix)
    except ValueError:
        return "WRONG"
    postfix = to_postfix(infix)

    stack = []
    for elem in postfix:
        if elem.isdigit():
            stack.append(int(elem))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if elem == "+":
                stack.append(operand1 + operand2)
            elif elem == "-":
                stack.append(operand1 - operand2)
            elif elem == "*":
                stack.append(operand1 * operand2)

    return stack.pop()


def to_infix(string) -> list[str]:

    n = len(string)

    infix = []
    i = 0
    while i < n:
        if string[i] == " ":
            i += 1
        elif string[i].isdigit():
            num = []
            while i < n and string[i].isdigit():
                num.append(string[i])
                i += 1
            infix.append("".join(num))
        else:
            infix.append(string[i])
            i += 1

    return infix


def validate(infix: list[str]) -> None:

    operators = ("+", "-", "*")

    prev_elem = ""
    bracket_count = 0
    for elem in infix:
        if elem.isalpha():
            raise ValueError
        if elem.isdigit() and (prev_elem.isdigit() or prev_elem == ")"):
            raise ValueError
        if elem in operators and (prev_elem in operators or prev_elem == "("):
            raise ValueError
        if elem == "(":
            if prev_elem.isdigit() or prev_elem == ")":
                raise ValueError
            bracket_count += 1
        if elem == ")":
            if prev_elem in operators or prev_elem == "(":
                raise ValueError
            bracket_count -= 1
            if bracket_count < 0:
                raise ValueError
        prev_elem = elem

    if infix[-1] in operators or infix[-1] == "(":
        raise ValueError

    if bracket_count != 0:
        raise ValueError
    if not (prev_elem.isdigit() or prev_elem == ")"):
        raise ValueError


def to_postfix(infix: list[str]) -> list[str]:

    postfix = []
    stack = []
    for elem in infix:
        if elem.isdigit():
            postfix.append(elem)
        elif elem in ("+", "-"):
            while stack and stack[-1] in ("+", "-", "*"):
                postfix.append(stack.pop())
            stack.append(elem)
        elif elem == "*":
            while stack and stack[-1] == "*":
                postfix.append(stack.pop())
            stack.append(elem)
        elif elem == "(":
            stack.append(elem)
        elif elem == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    return postfix


if __name__ == "__main__":
    result = main()
    print(result)
