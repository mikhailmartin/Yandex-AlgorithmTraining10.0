"""
Медиана

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Медиана последовательности — это элемент, который стоит в середине
отсортированной последовательности. Например, в последовательности 5, 1, 4, 2, 3
медианой является число 3. В случае массива чётной длины в рамках этой задачи
будем всегда брать элемент с меньшим индексом.

Для заданной последовательности выведите медианы каждого его префикса.
Гарантируется, что элементы последовательности не повторяются.


Формат ввода:
Первая строка входного файла содержит число элементов count (0 ≤ count ≤ 10^5).

Во второй строке через пробел указаны count различных чисел, по модулю не
превосходящих 10^9.


Формат вывода:
Выведите count чисел, разделяя их пробелами.


Пример 1
input: 5
input: 1 5 2 4 3
output: 1 1 2 2 3

Пример 2
input: 7
input: 10 1 2 3 9 5 8
output: 10 1 2 2 3 3 5


Примечание:
Для решения этой задачи создайте контейнер set и постоянно отслеживайте позицию
медианы в нём. Для этого вам пригодится iterator.
"""
import heapq
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    count: int
    nums: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        count = int(input())
        nums = list(map(int, input().split()))
        return cls(ProblemInput(count, nums))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        count = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return cls(ProblemInput(count, nums))

    def solve(self) -> list[int]:

        lo = []  # max-heap
        hi = []  # min-heap
        result = []
        for num in self.data.nums:
            if len(lo) == len(hi):
                heapq.heappush(lo, -heapq.heappushpop(hi, num))
            else:
                heapq.heappush(hi, -heapq.heappushpop(lo, -num))
            result.append(-lo[0])

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(*result)


if __name__ == "__main__":
    main()
