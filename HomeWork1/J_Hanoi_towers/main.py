import sys


def main(lines: list[str] | None = None) -> list[tuple[int, int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])

    res = []

    def hanoi(n: int, a: int, b: int) -> None:
        if n == 1:
            res.append((1, a, b))
        else:
            hanoi(n - 1, a, 6 - a - b)
            res.append((n, a, b))
            hanoi(n - 1, 6 - a - b, b)

    hanoi(n, 1, 3)

    return res


if __name__ == "__main__":
    result = main()
    for line in result:
        print(*line)
