import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    cities = []
    for i in range(n):
        x, y = map(int, lines[i + 1].split())
        cities.append((x, y))

    xs = []
    ys = []
    for x, y in cities:
        xs.append(x)
        ys.append(y)

    x_median = median(xs)
    y_median = median(ys)

    cities = set(cities)
    best_candidate = None
    min_total_dist = float("inf")
    for cx, cy in candidates(x_median, y_median):
        if (cx, cy) in cities:
            continue

        total_dist = sum(abs(cx - x) + abs(cy - y) for x, y in cities)

        if total_dist < min_total_dist:
            min_total_dist = total_dist
            best_candidate = (cx, cy)

    return best_candidate


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


def candidates(x_med: int | float, y_med: int | float):
    x_lo, x_hi = get_optimal_range(x_med)
    y_lo, y_hi = get_optimal_range(y_med)
    for cx in range(x_lo - 5, x_hi + 6):
        for cy in range(y_lo - 5, y_hi + 6):
            yield cx, cy


def get_optimal_range(median_val: int | float) -> tuple[int, int]:
    if isinstance(median_val, float):
        lo = int(median_val)
        hi = lo + 1
    else:
        lo = int(median_val)
        hi = int(median_val)
    return lo, hi


if __name__ == "__main__":
    result = main()
    print(*result)
