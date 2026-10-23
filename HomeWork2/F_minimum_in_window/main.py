import sys
from collections import deque


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    deq = deque()
    i = 0
    while i < k:
        num = nums[i]
        while deq and deq[-1] > num:
            deq.pop()
        deq.append(num)
        i += 1
    res = [deq[0]]

    left = 1
    while left < n - k + 1:
        right = left + k - 1
        while deq and deq[-1] > nums[right]:
            deq.pop()
        deq.append(nums[right])

        if deq[0] == nums[left-1]:
            deq.popleft()

        res.append(deq[0])
        left += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
