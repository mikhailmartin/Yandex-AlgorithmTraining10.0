import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    prices = list(map(int, lines[1].split()))

    res = [-1] * n
    stack = []
    for curr_i, curr_price in enumerate(prices):
        while stack and curr_price < stack[-1][1]:
            prev_i, prev_price = stack.pop()
            res[prev_i] = curr_i
        stack.append((curr_i, curr_price))

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
