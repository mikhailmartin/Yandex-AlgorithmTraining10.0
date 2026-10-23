import sys
import heapq


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    count = int(lines[0])
    nums = list(map(int, lines[1].split()))

    lo = []  # max-heap
    hi = []  # min-heap
    res = []
    for num in nums:
        if len(lo) == len(hi):
            heapq.heappush(lo, -heapq.heappushpop(hi, num))
        else:
            heapq.heappush(hi, -heapq.heappushpop(lo, -num))
        res.append(-lo[0])

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
