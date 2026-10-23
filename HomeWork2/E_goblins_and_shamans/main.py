import sys
from collections import deque


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    res = []
    left = deque()
    right = deque()
    for i in range(n):
        query = lines[i+1]
        if query.startswith("+"):
            _, i = query.split()
            right.append(i)
            if len(left) < len(right):
                left.append(right.popleft())
        elif query.startswith("*"):
            _, i = query.split()
            if len(left) == len(right):
                left.append(i)
            else:
                right.appendleft(i)
        elif query == "-":
            res.append(left.popleft())
            if len(left) < len(right):
                left.append(right.popleft())

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
