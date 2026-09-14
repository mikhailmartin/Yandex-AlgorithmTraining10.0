"""
Пираты Баренцева моря

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским
битвам. Игровое поле представляет собой квадрат из N×N клеток, на котором
расположено N кораблей (каждый корабль занимает одну клетку).

Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить
все N кораблей в одном столбце. За один ход можно передвинуть один корабль в
одну из четырёх соседних по стороне клеток. Номер столбца, в котором будут
выстроены корабли, не важен. Определите минимальное количество ходов,
необходимых для построения кораблей в одном столбце. В начале и процессе игры
никакие два корабля не могут находиться в одной клетке.


Формат ввода:
В первой строке входных данных задаётся число N (1 ≤ N ≤ 100).

В каждой из следующих N строк задаются координаты корабля:
сначала номер строки, затем номер столбца (нумерация начинается с единицы).


Формат вывода:
Выведите одно число — минимальное количество ходов, необходимое для построения.


Примечание:
В примере необходимо выстроить корабли в столбце номер 2. Для этого необходимо
переставить корабль из клетки 3 3 в клетку 3 2 за один ход, а корабль из клетки
1 1 в клетку 2 2 за два хода. Существуют и другие варианты перестановки
кораблей, однако ни в одном из них нет меньше трёх ходов.


Пример
input: 3
input: 1 2
input: 3 3
input: 1 1
output: 3
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    ships: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        ships = []
        for _ in range(n):
            x, y = map(int, input().split())
            ships.append((x, y))
        return cls(ProblemInput(n, ships))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        ships = []
        for i in range(n):
            x, y = map(int, lines[i+1].split())
            ships.append((x, y))
        return cls(ProblemInput(n, ships))

    def solve(self) -> tuple[int, int]:

        ships = self.data.ships
        n = self.data.n

        # ищем наиболее подходящий столбец
        ys = [y for _, y in ships]
        y_median = self.median(ys)
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
            column = [(i, col) for i in range(1, n+1)]
            for p1, p2 in zip(ranked, column):
                turns += self.dist(p1, p2)
            min_turns = min(min_turns, turns)

        return min_turns

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
    def dist(point1: tuple[int, int], point2: tuple[int, int]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
