"""
Количество обменов в heapify

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Процедура heapify преобразует неупорядоченный массив в двоичную кучу, на вершине
которой располагается максимальный элемент:

void heapify(vector<int> &a) {
    for (int i = a.size() - 1; i >= 0; i-)
        down(a, i);
}

Определите, сколько раз будет произведён обмен местами двух элементов массива
при выполнении heapify.


Формат ввода:
Первая строка содержит целое число N (1 ≤ N ≤ 10^4) — количество элементов массива.
Вторая строка содержит N целых чисел A_i (−2^31 ≤ A_i < 2^31) — элементы массива.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: 5
input: 1 2 3 4 5
output: 3

Пример 2
input: 5
input: 5 4 3 2 1
output: 0

Пример 3
input: 5
input: 5 3 1 2 4
output: 1
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
        self.count: int = 0

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

        n = self.data.n
        array = self.data.array

        count = 0
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
                    count += 1
                else:
                    break

        return count


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
