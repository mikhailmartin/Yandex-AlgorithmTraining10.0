import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    nums = list(map(int, lines[0].split()))
    n = nums[0]
    heights = nums[1:]

    right = [n] * n  # ближайший меньше справа
    stack = []
    for curr_i, curr_height in enumerate(heights):
        while stack and curr_height < stack[-1][1]:
            prev_i, prev_height = stack.pop()
            right[prev_i] = curr_i
        stack.append((curr_i, curr_height))

    left = [-1] * n  # ближайший меньше слева
    for curr_i in range(n - 1, -1, -1):
        curr_height = heights[curr_i]
        while stack and curr_height < stack[-1][1]:
            prev_i, prev_height = stack.pop()
            left[prev_i] = curr_i
        stack.append((curr_i, curr_height))

    max_area = -1
    for height, li, ri in zip(heights, left, right):
        width = ri - li - 1
        area = width * height
        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    result = main()
    print(result)
