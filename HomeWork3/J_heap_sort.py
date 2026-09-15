"""
Пирамидальная сортировка

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Отсортируйте данный массив. Используйте пирамидальную сортировку.


Формат ввода:
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10^5.
Далее задаются N целых чисел, не превосходящих по абсолютной величине 10^9.


Формат вывода:
Выведите эти числа в порядке неубывания.


Пример 1
input: 1
input: 1
output: 1


Пример 2
input: 2
input: 3 1
output: 1 3
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    array: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        array = list(map(int, input().split()))
        return cls(ProblemInput(n, array))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        array = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, array))

    def solve(self) -> list[int]:

        n = self.data.n
        array = self.data.array

        # сделали кучу максимумов, просеяв каждый узел вниз
        for i in range(n-1, -1, -1):
            while True:
                left_i = 2 * i + 1
                right_i = 2 * i + 2
                if left_i > n - 1:
                    break
                elif right_i > n - 1:
                    child_i = left_i
                elif array[left_i] > array[right_i]:
                    child_i = left_i
                else:
                    child_i = right_i

                if array[i] < array[child_i]:
                    array[i], array[child_i] = array[child_i], array[i]
                    i = child_i
                else:
                    break

        # перестановки
        for j in range(n-1):
            # переставили
            array[0], array[-(j+1)] = array[-(j+1)], array[0]
            # просеяли вниз
            i = 0
            while True:
                left_i = 2 * i + 1
                right_i = 2 * i + 2
                if left_i > n - (1 + j + 1):
                    break
                elif right_i > n - (1 + j + 1):
                    child_i = left_i
                elif array[left_i] > array[right_i]:
                    child_i = left_i
                else:
                    child_i = right_i

                if array[i] < array[child_i]:
                    array[i], array[child_i] = array[child_i], array[i]
                    i = child_i
                else:
                    break

        return array


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
