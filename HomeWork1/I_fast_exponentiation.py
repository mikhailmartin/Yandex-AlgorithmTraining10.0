"""
Быстрое возведение в степень

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно
воспользоваться следующими рекуррентными соотношениями:
a^n = (a^2)^{n/2} при чётном n,
a^n = a * a^{n-1} при нечётном n.

Реализуйте алгоритм быстрого возведения в степень. Если вы всё сделаете
правильно, то сложность вашего алгоритма будет O(log n).


Формат ввода:
Вводится действительное число a и целое число n.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: 2
input: 1
output: 2

Пример 2
input: 2
input: 2
output: 4

Пример 3
input: 2
input: 3
output: 8
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    num: float
    power: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        num = float(input())
        power = int(input())
        return cls(ProblemInput(num, power))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        num = float(lines[0])
        power = int(lines[1])
        return cls(ProblemInput(num, power))

    def solve(self) -> int:

        num = self.data.num
        power = self.data.power

        result = 1
        while power:
            if power % 2 == 1:
                result *= num
            num *= num
            power //= 2

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
