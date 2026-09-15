"""
Сортировка слиянием

Ограничение времени - 15 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.

На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с
помощью уже реализованной функции.


Формат ввода:
В первой строке входного файла содержится число N — количество элементов массива
(0 ≤ N ≤ 10^6).
Во второй строке содержатся N целых чисел a_i, разделённых пробелами
(−10^9 ≤ a_i ≤ 10^9).


Формат вывода:
Выведите результат сортировки, то есть N целых чисел, разделённых пробелами,
в порядке неубывания.


Пример
input: 5
input: 1 5 2 4 3
output: 1 2 3 4 5


Примечание:
Используйте функцию, реализованную в предыдущей задаче.
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
        if self.data.n == 0:
            return []
        return self.merge_sort(self.data.array)

    def merge_sort(self, array: list[int]) -> list[int]:

        n = len(array)

        if n == 1:
            return array
        else:
            mid = n // 2
            left_subarray = array[:mid]
            left_sorted = self.merge_sort(left_subarray)
            right_subarray = array[mid:]
            right_sorted = self.merge_sort(right_subarray)
            return self.merge(left_sorted, right_sorted)

    @staticmethod
    def merge(array1: list[int], array2: list[int]) -> list[int]:

        n = len(array1)
        m = len(array2)

        result = [0] * (m + n)
        i = 0
        j = 0
        k = 0
        while i < n and j < m:
            if array1[i] < array2[j]:
                result[k] = array1[i]
                i += 1
            else:
                result[k] = array2[j]
                j += 1
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

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
