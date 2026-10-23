import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    if n == 0:
        return []

    def partition(left: int, right: int) -> None:

        while left < right:
            mid = (left + right) // 2
            v1, v2, v3 = nums[left], nums[mid], nums[right]
            if v1 > v2: v1, v2 = v2, v1
            if v2 > v3: v2, v3 = v3, v2
            if v1 > v2: v1, v2 = v2, v1
            x = v2

            lt = left
            gt = right
            i = left
            while i <= gt:
                if nums[i] < x:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > x:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            left_size = lt - left
            right_size = right - gt

            if left_size < right_size:
                partition(left=left, right=lt-1)
                left = gt + 1
            else:
                partition(left=gt+1, right=right)
                right = lt - 1

    partition(left=0, right=n-1)

    return nums


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
