import sys
import heapq


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    cost = 0
    heapq.heapify(nums)
    while len(nums) > 1:
        operand1 = heapq.heappop(nums)
        operand2 = heapq.heappop(nums)
        res = operand1 + operand2
        heapq.heappush(nums, res)
        cost += res * 0.05

    return f"{cost:.2f}"


if __name__ == "__main__":
    result = main()
    print(result)
