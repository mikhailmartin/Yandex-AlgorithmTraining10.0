import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    array = list(map(int, lines[1].split()))

    inversions = 0
    if n == 0:
        return inversions

    def merge_sort(arr: list[int]) -> list[int]:
        l = len(arr)
        if l <= 1:
            return arr
        else:
            mid = l // 2
            left_sorted = merge_sort(arr[:mid])
            right_sorted = merge_sort(arr[mid:])
            return merge(left_sorted, right_sorted)

    def merge(arr1: list[int], arr2: list[int]) -> list[int]:

        nonlocal inversions

        n = len(arr1)
        m = len(arr2)

        res = [0] * (m + n)
        i = 0
        j = 0
        k = 0

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                res[k] = arr1[i]
                i += 1
            else:
                res[k] = arr2[j]
                j += 1
                inversions += n - i
            k += 1

        while i < n:
            res[k] = arr1[i]
            i += 1
            k += 1

        while j < m:
            res[k] = arr2[j]
            j += 1
            k += 1

        return res

    merge_sort(array)

    return inversions


if __name__ == "__main__":
    result = main()
    print(result)
