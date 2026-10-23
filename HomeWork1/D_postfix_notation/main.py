import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    postfix = lines[0]

    stack = []
    for elem in postfix.split():
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


if __name__ == "__main__":
    result = main()
    print(result)
