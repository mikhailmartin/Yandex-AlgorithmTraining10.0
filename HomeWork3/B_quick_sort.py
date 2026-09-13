"""
Быстрая сортировка

Ограничение времени - 10 секунд
Ограничение памяти - 512Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.

На каждом шаге выбирайте опорный элемент и выполняйте partition относительно
него. Затем рекурсивно запуститесь от двух частей, на которые разбился исходный
массив.


Формат ввода:
В первой строке входного файла содержится число N — количество элементов массива
(0 ≤ N ≤ 10^6).
Во второй строке содержатся N целых чисел a_i, разделённых пробелами
(−10^9 ≤ a_i ≤ 10^9).


Формат вывода:
Выведите результат сортировки, то есть N целых чисел, разделенных пробелами.


Пример
input: 5
input: 1 5 2 4 3
output: 1 2 3 4 5


Примечание:
Используйте функцию, реализованную в предыдущей задаче.
"""
import sys
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    nums: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        input_data = sys.stdin.buffer.read().split()
        n = int(input_data[0])
        nums = [int(num) for num in input_data[1:n + 1]]
        return cls(ProblemInput(n, nums))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, nums))

    def solve(self) -> list[int]:

        if self.data.n == 0:
            return []

        self.partition(left=0, right=self.data.n-1)

        return self.data.nums

    def partition(self, left: int, right: int) -> None:

        nums = self.data.nums

        while left < right:
            mid = (left + right) // 2
            v1, v2, v3 = nums[left], nums[mid], nums[right]
            if v1 > v2: v1, v2 = v2, v1
            if v2 > v3: v2, v3 = v3, v2
            if v1 > v2: v1, v2 = v2, v1
            x = v2

            lt = left
            gt = right
            i = left
            while i <= gt:
                if nums[i] < x:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > x:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            left_size = lt - left
            right_size = right - gt

            if left_size < right_size:
                self.partition(left=left, right=lt-1)
                left = gt + 1
            else:
                self.partition(left=gt+1, right=right)
                right = lt - 1


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
