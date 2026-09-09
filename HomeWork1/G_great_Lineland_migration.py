"""
Великое Лайнландское переселение

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором
располагаются N городов, последовательно пронумерованных от 0 до N - 1.
Направление в сторону от первого города к нулевому названо западным, а в
обратную — восточным.

Когда в Лайнландии неожиданно начался кризис, все жители мира стали испытывать
глубокое смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся
лучше, чем на западе.

Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами
отправились на восток, покинув родные улицы, и двигались до тех пор, пока не
приходили в город, в котором средняя цена проживания была меньше, чем в родном.


Формат ввода:
В первой строке дано одно число N (2 ≤ N ≤ 10^5) — количество городов в Лайнландии.
Во второй строке дано N чисел a_i (0 ≤ a_i ≤ 10^9) — средняя цена проживания в
городах с нулевого по (N - 1)-й соответственно.


Формат вывода:
Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города,
в который переселятся его изначальные жители. Если жители города не остановятся
в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто,
выведите -1.


Пример
input: 10
input: 1 2 3 2 1 4 2 5 3 1
output: -1 4 3 4 -1 6 9 8 9 -1
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    prices: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        prices = list(map(int, input().split()))
        return cls(ProblemInput(n, prices))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        prices = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, prices))

    def solve(self) -> list[int]:

        result = [-1] * self.data.n
        stack = []
        for curr_i, curr_price in enumerate(self.data.prices):
            while stack and curr_price < stack[-1][1]:
                prev_i, prev_price = stack.pop()
                result[prev_i] = curr_i
            stack.append((curr_i, curr_price))

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(*result)


if __name__ == "__main__":
    main()
