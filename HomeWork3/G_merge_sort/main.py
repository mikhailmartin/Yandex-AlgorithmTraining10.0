import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    array = list(map(int, lines[1].split()))

    if n == 0:
        return []

    return merge_sort(array)


def merge_sort(arr: list[int]) -> list[int]:

    n = len(arr)

    if n == 1:
        return arr
    else:
        mid = n // 2
        left_subarray = arr[:mid]
        left_sorted = merge_sort(left_subarray)
        right_subarray = arr[mid:]
        right_sorted = merge_sort(right_subarray)
        return merge(left_sorted, right_sorted)


def merge(arr1: list[int], arr2: list[int]) -> list[int]:

    n = len(arr1)
    m = len(arr2)

    result = [0] * (m + n)
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1

    while i < n:
        result[k] = arr1[i]
        i += 1
        k += 1

    while j < m:
        result[k] = arr2[j]
        j += 1
        k += 1

    return result


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
