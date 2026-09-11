"""
Минимум в окне

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Рассмотрим последовательность целых чисел длины n. По ней с шагом 1 двигается
«окно» длины k, то есть сначала в «окне» видны первые k чисел, на следующем
шаге в «окне» уже будут находиться k чисел, начиная со второго, и так далее до
конца последовательности. Требуется для каждого положения «окна» определить
минимум в нём.


Формат ввода:
В первой строке входных данных содержатся два натуральных числа n и k
(n ≤ 150000, k ≤ 10000, k ≤ n) – длины последовательности и «окна»,
соответственно. На следующей строке находятся n чисел – сама последовательность.


Формат вывода:
Выходые данные должны содержать n − k + 1 строк – минимумы для каждого положения
«окна».


Пример
input: 7 3
input: 1 3 2 4 5 3 1
output: 1
output: 2
output: 2
output: 3
output: 1
"""
from collections import deque
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    k: int
    nums: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        return cls(ProblemInput(n, k, nums))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, k = map(int, lines[0].split())
        nums = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, k, nums))

    def solve(self) -> list[str]:

        n = self.data.n
        k = self.data.k
        nums = self.data.nums

        deq = deque()
        i = 0
        while i < k:
            num = nums[i]
            while deq and deq[-1] > num:
                deq.pop()
            deq.append(num)
            i += 1
        result = [deq[0]]

        left = 1
        while left < n - k + 1:
            right = left + k - 1
            while deq and deq[-1] > nums[right]:
                deq.pop()
            deq.append(nums[right])

            if deq[0] == nums[left-1]:
                deq.popleft()

            result.append(deq[0])
            left += 1

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
