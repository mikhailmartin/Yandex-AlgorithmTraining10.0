import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    num = float(lines[0])
    power = int(lines[1])

    res = 1
    while power:
        if power % 2 == 1:
            res *= num
        num *= num
        power //= 2

    return res


if __name__ == "__main__":
    result = main()
    print(result)
