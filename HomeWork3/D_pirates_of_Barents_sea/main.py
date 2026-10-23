import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    ships = []
    for i in range(n):
        x, y = map(int, lines[i+1].split())
        ships.append((x, y))

    # ищем наиболее подходящий столбец
    ys = [y for _, y in ships]
    y_median = median(ys)
    if isinstance(y_median, int):
        cols = [y_median]
    else:
        lo = int(y_median)
        hi = lo + (y_median > lo)
        cols = [lo, hi]

    min_turns = float("+inf")
    for col in cols:
        turns = 0
        ranked = sorted(ships, key=lambda p: p[0])
        column = [(i, col) for i in range(1, n + 1)]
        for p1, p2 in zip(ranked, column):
            turns += dist(p1, p2)
        min_turns = min(min_turns, turns)

    return min_turns


def median(elements: list[int]) -> int | float:

    k = len(elements)
    if k % 2 == 1:
        median_i = k // 2
        median = nth_element(elements, median_i)
    else:
        left_median_i = (k - 1) // 2
        left_median = nth_element(elements, left_median_i)
        right_median_i = k // 2
        right_median = nth_element(elements, right_median_i)
        median = (left_median + right_median) / 2
        median = int(median) if median.is_integer() else median

    return median


def nth_element(elements: list[int], n: int) -> int:

    def partition(left: int, right: int) -> None:

        if left >= right:
            return

        pivot = elements[(left + right) // 2]

        lt = left
        gt = right
        i = left
        while i <= gt:
            if elements[i] < pivot:
                elements[i], elements[lt] = elements[lt], elements[i]
                lt += 1
                i += 1
            elif elements[i] > pivot:
                elements[i], elements[gt] = elements[gt], elements[i]
                gt -= 1
            else:
                i += 1

        if n < lt:
            partition(left, lt-1)
        elif gt < n:
            partition(gt+1, right)

    partition(left=0, right=len(elements)-1)

    return elements[n]


def dist(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    result = main()
    print(result)
