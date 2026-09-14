"""
Столица

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В некотором царстве, в некотором государстве было N городов, и все они, судя по
главной карте императора, имели целые координаты. В те годы леса были дремучие,
дороги же строить умели только параллельно осям координат, так что расстояние
между двумя городами определялось как ∣x_1 − x_2∣ + ∣y_1 − y_2∣.

Император решил построить N+1-ый город и сделать его столицей своего
государства, при этом координаты столицы также должны быть целыми. Место для
столицы следует выбрать так, чтобы среднее арифметическое расстояний между
столицей и остальными городами было как можно меньше. Однако, разумеется,
столицу нельзя строить на месте существующего города.

Нелёгкая задача выбрать место для столицы поручена Вам.


Формат ввода:
В первой строке вводится число N - количество городов (1 ≤ N ≤ 100). Следующие N
строк содержат координаты городов - пары целых чисел, не превышающих 1000 по
абсолютной величине.


Формат вывода:
Выведите два целых числа - координаты точки, где следует построить столицу. Если
решений несколько, выведите любое.


Пример 1
input: 8
input: 0 0
input: 1 0
input: 2 0
input: 0 1
input: 2 1
input: 0 2
input: 1 2
input: 2 2
output: 1 1

Пример 2
input: 4
input: 0 0
input: 1 1
input: 0 1
input: 1 0
output: 0 -1
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    cities: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        cities = []
        for _ in range(n):
            x, y = map(int, input().split())
            cities.append((x, y))
        return cls(ProblemInput(n, cities))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        cities = []
        for i in range(n):
            x, y = map(int, lines[i+1].split())
            cities.append((x, y))
        return cls(ProblemInput(n, cities))

    def solve(self) -> tuple[int, int]:

        xs = []
        ys = []
        for x, y in self.data.cities:
            xs.append(x)
            ys.append(y)

        x_median = self.median(xs)
        y_median = self.median(ys)

        cities = set(self.data.cities)
        best_candidate = None
        min_total_dist = float("inf")
        for cx, cy in self.candidates(x_median, y_median):
            if (cx, cy) in cities:
                continue

            total_dist = sum(abs(cx - x) + abs(cy - y) for x, y in self.data.cities)

            if total_dist < min_total_dist:
                min_total_dist = total_dist
                best_candidate = (cx, cy)

        return best_candidate

    def median(self, elements: list[int]) -> int | float:

        k = len(elements)
        if k % 2 == 1:
            median_i = k // 2
            median = self.nth_element(elements, median_i)
        else:
            left_median_i = (k - 1) // 2
            left_median = self.nth_element(elements, left_median_i)
            right_median_i = k // 2
            right_median = self.nth_element(elements, right_median_i)
            median = (left_median + right_median) / 2
            median = int(median) if median.is_integer() else median

        return median

    @staticmethod
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

    @staticmethod
    def candidates(x_med: int | float, y_med: int | float):
        x_lo, x_hi = Solver._get_optimal_range(x_med)
        y_lo, y_hi = Solver._get_optimal_range(y_med)
        for cx in range(x_lo - 5, x_hi + 6):
            for cy in range(y_lo - 5, y_hi + 6):
                yield cx, cy

    @staticmethod
    def _get_optimal_range(median_val: int | float) -> tuple[int, int]:
        if isinstance(median_val, float):
            lo = int(median_val)
            hi = lo + 1
        else:
            lo = int(median_val)
            hi = int(median_val)
        return lo, hi


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(*result)


if __name__ == "__main__":
    main()
