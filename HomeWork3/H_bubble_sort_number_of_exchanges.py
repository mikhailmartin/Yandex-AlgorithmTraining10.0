"""
Сортировка пузырьком: количество обменов

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Определите, сколько обменов сделает алгоритм пузырьковой сортировки по
возрастанию для данного массива.


Формат ввода:
На первой строке дано число N (1 ≤ N ≤ 100_000) – количество элементов в
массиве. На второй строке – сам массив. Гарантируется, что все элементы массива
различны и не превышают по модулю 10^9.


Формат вывода:
Выведите одно число – количество обменов пузырьковой сортировки.


Пример 1
input: 5
input: 1 2 3 4 5
output: 0

Пример 2
input: 5
input: 5 4 3 2 1
output: 10
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
        self.inversions: int = 0

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

    def solve(self) -> int:

        if self.data.n == 0:
            return 0

        self.merge_sort(self.data.array)

        return self.inversions

    def merge_sort(self, array: list[int]) -> list[int]:

        n = len(array)

        if n <= 1:
            return array
        else:
            mid = n // 2
            left_sorted = self.merge_sort(array[:mid])
            right_sorted = self.merge_sort(array[mid:])
            return self.merge(left_sorted, right_sorted)

    def merge(self, array1: list[int], array2: list[int]) -> list[int]:

        n = len(array1)
        m = len(array2)

        result = [0] * (m + n)
        i = 0
        j = 0
        k = 0

        while i < n and j < m:
            if array1[i] <= array2[j]:
                result[k] = array1[i]
                i += 1
            else:
                result[k] = array2[j]
                j += 1
                self.inversions += n - i
            k += 1

        while i < n:
            result[k] = array1[i]
            i += 1
            k += 1

        while j < m:
            result[k] = array2[j]
            j += 1
            k += 1

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
