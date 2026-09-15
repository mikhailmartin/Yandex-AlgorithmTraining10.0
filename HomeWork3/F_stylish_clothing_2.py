"""
Стильная одежда 2

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Глеб обожает шоппинг. Как-то раз он загорелся идеей подобрать себе кепку, майку,
штаны и ботинки так, чтобы выглядеть в них максимально стильно. В понимании
Глеба стильность одежды тем больше, чем меньше разница в цвете элементов его
одежды.

В наличии имеется N_1 кепок, N_2 маек, N_3 штанов и N_4 пар ботинок
(1 ≤ N_i ≤ 100_000). Про каждый элемент одежды известен его цвет (целое число от
1 до 100_000). Комплект одежды — это одна кепка, майка, штаны и одна пара
ботинок. Каждый комплект характеризуется максимальной разницей между любыми
двумя его элементами. Помогите Глебу выбрать максимально стильный комплект, то
есть комплект с минимальной разницей цветов.


Формат ввода:
Для каждого типа одежды i (i = 1, 2, 3, 4) сначала вводится количество N_i
элементов одежды этого типа, далее в следующей строке — последовательность из
N_i целых чисел, описывающих цвета элементов. Все четыре типа подаются на вход
последовательно, начиная с кепок и заканчивая ботинками. Все вводимые числа
целые, положительные и не превосходят 100_000.


Формат вывода:
Выведите четыре целых числа — цвета соответственно для кепки, майки, штанов и
ботинок, которые должен выбрать Глеб из имеющихся для того, чтобы выглядеть
наиболее стильно. Если ответов несколько, выведите любой.


Пример 1
input: 3
input: 1 2 3
input: 2
input: 1 3
input: 2
input: 3 4
input: 2
input: 2 3
output: 3 3 3 3

Пример 2
input: 1
input: 5
input: 4
input: 3 6 7 10
input: 4
input: 18 3 9 11
input: 1
input: 20
output: 5 6 9 20
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    ns: list[int]
    arrays: list[list[int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        ns = []
        arrays = []
        for _ in range(4):
            n = int(input())
            ns.append(n)
            array = list(map(int, input().split()))
            arrays.append(array)
        return cls(ProblemInput(ns, arrays))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        ns = []
        arrays = []
        for i in range(4):
            n = int(lines[2 * i])
            ns.append(n)
            array = list(map(int, lines[2 * i + 1].split()))
            arrays.append(array)
        return cls(ProblemInput(ns, arrays))

    def solve(self) -> tuple[int, ...]:

        ns = self.data.ns
        arrays = self.data.arrays
        N = len(arrays)

        for array in arrays:
            array.sort()

        idxes = [0] * N
        look = [arrays[i][idxes[i]] for i in range(N)]
        min_idx, min_value = self.argmin(look)
        max_idx, max_value = self.argmax(look)
        best_style = max_value - min_value
        best_look = tuple(look)
        while all(idxes[i] < ns[i] for i in range(N)):
            look = [arrays[i][idxes[i]] for i in range(N)]
            min_idx, min_value = self.argmin(look)
            max_idx, max_value = self.argmax(look)
            style = max_value - min_value
            if style < best_style:
                best_style = style
                best_look = tuple(look)
            idxes[min_idx] += 1

        return best_look

    @staticmethod
    def argmin(array: list[int]) -> tuple[int, int]:
        min_idx, min_value = -1, 100_001
        for i, value in enumerate(array):
            if value < min_value:
                min_idx, min_value = i, value
        return min_idx, min_value

    @staticmethod
    def argmax(array: list[int]) -> tuple[int, int]:
        max_idx, max_value = -1, -1
        for i, value in enumerate(array):
            if value > max_value:
                max_idx, max_value = i, value
        return max_idx, max_value


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
