import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    arr1 = list(map(int, lines[1].split()))
    m = int(lines[2])
    arr2 = list(map(int, lines[3].split()))

    res = [0] * (m + n)
    i = 0
    j = 0
    k = 0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            res[k] = arr1[i]
            i += 1
        else:
            res[k] = arr2[j]
            j += 1
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


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
