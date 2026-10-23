import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    infix = lines[0]

    postfix = to_postfix(infix)

    stack = []
    for elem in postfix:
        if elem.isdigit():
            stack.append(bool(int(elem)))
        elif elem == "!":
            operand = stack.pop()
            stack.append(not operand)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if elem == "|":
                stack.append(operand1 | operand2)
            elif elem == "^":
                stack.append(operand1 ^ operand2)
            elif elem == "&":
                stack.append(operand1 & operand2)

    return 1 if stack.pop() else 0


def to_postfix(infix: str) -> list[str]:

    postfix = []
    stack = []
    for char in infix:
        if char.isdigit():
            postfix.append(char)
        elif char in ("|", "^"):
            while stack and stack[-1] in ("|", "^", "&", "!"):
                postfix.append(stack.pop())
            stack.append(char)
        elif char == "&":
            while stack and stack[-1] in ("&", "!"):
                postfix.append(stack.pop())
            stack.append(char)
        elif char == "!":
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()

    while stack:
        postfix.append(stack.pop())

    return postfix


if __name__ == "__main__":
    result = main()
    print(result)
