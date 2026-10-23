import sys
from typing import Literal


def main(lines: list[str] | None = None) -> Literal["yes", "no"]:

    lines = lines or sys.stdin.read().splitlines()

    sequence = lines[0]

    opened = {"(", "[", "{"}
    closed = {")": "(", "]": "[", "}": "{"}

    stack = []
    for char in sequence:
        if char in opened:
            stack.append(char)
        else:
            if stack and stack[-1] == closed[char]:
                stack.pop()
            else:
                return "no"

    return "no" if stack else "yes"


if __name__ == "__main__":
    result = main()
    print(result)
