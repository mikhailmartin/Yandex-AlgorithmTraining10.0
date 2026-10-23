import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))

    # сделали кучу максимумов, просеяв каждый узел вниз
    for i in range(n - 1, -1, -1):
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
            else:
                break

    # перестановки
    for j in range(n - 1):
        # переставили
        arr[0], arr[-(j + 1)] = arr[-(j + 1)], arr[0]
        # просеяли вниз
        i = 0
        while True:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            if left_i > n - (1 + j + 1):
                break
            elif right_i > n - (1 + j + 1):
                child_i = left_i
            elif arr[left_i] > arr[right_i]:
                child_i = left_i
            else:
                child_i = right_i

            if arr[i] < arr[child_i]:
                arr[i], arr[child_i] = arr[child_i], arr[i]
                i = child_i
            else:
                break

    return arr


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
