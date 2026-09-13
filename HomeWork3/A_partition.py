"""
Partition

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Базовым алгоритмом для быстрой сортировки является алгоритм partition, который
разбивает набор элементов на две части относительно заданного предиката.
По сути элементы массива просто меняются местами так, что левее некоторой точки
в нём после этой операции лежат элементы, удовлетворяющие заданному предикату,
а справа — не удовлетворяющие ему. Например, при сортировке можно использовать
предикат «меньше опорного», что при оптимальном выборе опорного элемента может
разбить массив на две примерно равные части.

Напишите алгоритм partition в качестве первого шага для написания быстрой
сортировки.


Формат ввода:
В первой строке входного файла содержится число N — количество элементов массива
(0 ≤ N ≤ 10^6).
Во второй строке содержатся N целых чисел a_i, разделённых пробелами
(−10^9 ≤ a_i ≤ 10^9).
В третьей строке содержится опорный элемент x (−10^9 ≤ x ≤ 10^9).
Заметьте, что x не обязательно встречается среди a_i.


Формат вывода:
Выведите результат работы вашего алгоритма при использовании предиката
«меньше x»: в первой строке выведите число элементов массива, меньших x, а во
второй — количество всех остальных.


Пример 1
input: 5
input: 1 9 4 2 3
input: 3
output: 2
output: 3

Пример 2
input: 0
input:
input: 0
output: 0
output: 0

Пример 3
input: 1
input: 0
input: 0
output: 0
output: 1


Примечание:
Советуем реализовать функцию, которая принимает на вход предикат и пару
итераторов, задающих массив (или массив и два индекса в нём), а возвращает точку
разбиения, то есть итератор (индекс) на конец части, которая содержит элементы,
удовлетворяющие заданному предикату.

В таком виде вам будет удобно использовать эту функцию для реализации сортировки.
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    nums: list[int]
    x: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        nums = list(map(int, input().split()))
        x = int(input())
        return cls(ProblemInput(n, nums, x))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        x = int(lines[2])
        return cls(ProblemInput(n, nums, x))

    def solve(self) -> tuple[int, int]:

        if self.data.n == 0:
            return 0, 0

        left = self.partition(self.data.x, left=0, right=self.data.n-1)
        less = left + 1 if self.data.nums[left] < self.data.x else left
        more = self.data.n - less

        return less, more

    def partition(self, x: int, left: int, right: int) -> int:

        nums = self.data.nums

        while left < right:
            while left < right and nums[left] < x:
                left += 1
            while left < right and nums[right] >= x:
                right -=1
            nums[left], nums[right] = nums[right], nums[left]

        return left


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result[0])
    print(result[1])


if __name__ == "__main__":
    main()
