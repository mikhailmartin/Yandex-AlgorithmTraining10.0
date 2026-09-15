"""
Слияние

Ограничение времени - 5 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Базовый алгоритм для сортировки слиянием — алгоритм слияния двух упорядоченных
массивов в один упорядоченный массив. Эта операция выполняется за линейное время
с линейным потреблением памяти. Реализуйте слияние двух массивов в качестве
первого шага для написания сортировки слиянием.


Формат ввода:
В первой строке входного файла содержится число N — количество элементов первого
массива (0 ≤ N ≤ 10^6).
Во второй строке содержатся N целых чисел a_i, разделённых пробелами,
отсортированные по неубыванию (−10^9 ≤ a_i ≤ 10^9).
В третьей строке входного файла содержится число M — количество элементов
второго массива (0 ≤ M ≤ 10^6).
В третьей строке содержатся M целых чисел b_i, разделённых пробелами,
отсортированные по неубыванию (−10^9 ≤ b_i ≤ 10^9).


Формат вывода:
Выведите результат слияния этих двух массивов, то есть M + N целых чисел,
разделённых пробелами, в порядке неубывания.


Пример 1
input: 5
input: 1 3 5 5 9
input: 3
input: 2 5 6
output: 1 2 3 5 5 5 6 9

Пример 2
input: 1
input: 0
input: 0
output: 0

Пример 3
input: 0
input:
input: 1
input: 0
output: 0
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    array1: list[int]
    m: int
    array2: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        array1 = list(map(int, input().split()))
        m = int(input())
        array2 = list(map(int, input().split()))
        return cls(ProblemInput(n, array1, m, array2))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        array1 = list(map(int, lines[1].split()))
        m = int(lines[2])
        array2 = list(map(int, lines[3].split()))
        return cls(ProblemInput(n, array1, m, array2))

    def solve(self) -> list[int]:

        n = self.data.n
        array1 = self.data.array1
        m = self.data.m
        array2 = self.data.array2

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
