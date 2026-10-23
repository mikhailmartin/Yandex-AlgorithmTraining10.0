import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    x = int(lines[2])

    if n == 0:
        return 0, 0

    def partition(pivot: int, left: int, right: int) -> int:
        while left < right:
            while left < right and nums[left] < pivot:
                left += 1
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return left

    left = partition(x, left=0, right=n-1)
    less = left + 1 if nums[left] < x else left
    more = n - less

    return less, more


if __name__ == "__main__":
    result = main()
    print(result[0])
    print(result[1])
