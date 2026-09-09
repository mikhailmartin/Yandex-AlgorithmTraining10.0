"""
Гистограмма и прямоугольник

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Гистограмма является многоугольником, сформированным из последовательности
прямоугольников, выровненных на общей базовой линии. Прямоугольники имеют равную
ширину, но могут иметь различные высоты. Например, фигура слева показывает
гистограмму, которая состоит из прямоугольников с высотами 2, 1, 4, 5, 1, 3, 3.
Все прямоугольники на этом рисунке имеют ширину, равную 1.

Обычно гистограммы используются для представления дискретных распределений,
например, частоты символов в текстах. Отметьте, что порядок прямоугольников
очень важен. Вычислите область самого большого прямоугольника в гистограмме,
который также находится на общей базовой линии. На рисунке справа заштрихованная
фигура является самым большим выровненным прямоугольником на изображенной
гистограмме.


Формат ввода:
Сначала записано число N (0 < N ≤ 10^6) — количество прямоугольников гистограммы.
Затем в той же строке записаны N целых чисел h_1, ..., h_n, где 0 ≤ h_i ≤10^9.
Эти числа обозначают высоты прямоугольников гистограммы слева направо. Ширина
каждого прямоугольника равна 1.


Формат вывода:
Выведите площадь самого большого прямоугольника в гистограмме. Помните, что этот
прямоугольник должен быть на общей базовой линии.


Пример
input: 7 2 1 4 5 1 3 3
output: 8
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    heights: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        nums = list(map(int, input().split()))
        n = nums[0]
        heights = nums[1:]
        return cls(ProblemInput(n, heights))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        nums = list(map(int, lines[0].split()))
        n = nums[0]
        heights = nums[1:]
        return cls(ProblemInput(n, heights))

    def solve(self) -> int:

        n = self.data.n
        heights = self.data.heights

        right = [n] * n  # ближайший меньше справа
        stack = []
        for curr_i, curr_height in enumerate(heights):
            while stack and curr_height < stack[-1][1]:
                prev_i, prev_height = stack.pop()
                right[prev_i] = curr_i
            stack.append((curr_i, curr_height))

        left = [-1] * n  # ближайший меньше слева
        for curr_i in range(n-1, -1, -1):
            curr_height = heights[curr_i]
            while stack and curr_height < stack[-1][1]:
                prev_i, prev_height = stack.pop()
                left[prev_i] = curr_i
            stack.append((curr_i, curr_height))

        max_area = -1
        for height, li, ri in zip(heights, left, right):
            width = ri - li - 1
            area = width * height
            max_area = max(max_area, area)

        return max_area


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
