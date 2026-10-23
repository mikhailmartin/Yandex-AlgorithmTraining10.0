import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))

    count = 0
    # сделали кучу максимумов, просеяв каждый узел вниз
    for i in range(n-1, -1, -1):
        while True:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            if left_i > n - 1:
                break
            elif right_i > n - 1:
                child_i = left_i
            elif arr[left_i] > arr[right_i]:
                child_i = left_i
            else:
                child_i = right_i

            if arr[i] < arr[child_i]:
                arr[i], arr[child_i] = arr[child_i], arr[i]
                i = child_i
                count += 1
            else:
                break

    return count


if __name__ == "__main__":
    result = main()
    print(result)
