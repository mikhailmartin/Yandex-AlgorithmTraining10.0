"""
Правильная скобочная последовательность

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных
скобок. Программа должна определить, является ли данная скобочная
последовательность правильной. Пустая последовательность является правильной.
Если A — правильная, то последовательности (A), [A], {A} — правильные.
Если A и B — правильные последовательности, то последовательность AB — правильная.


Формат ввода:
В единственной строке записана скобочная последовательность, содержащая не более
100000 скобок.


Формат вывода:
Если данная последовательность правильная, то программа должна вывести строку
"yes", иначе строку "no".


Пример 1
input: ()[]
output: yes

Пример 2
input: ([)]
output: no

Пример 3
input: (
output: no
"""
from dataclasses import dataclass
from typing import Literal, Self


@dataclass
class ProblemInput:
    sequence: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def sequence(self) -> str:
        return self.data.sequence

    @classmethod
    def from_stdin(cls) -> Self:
        sequence = input()
        return cls(ProblemInput(sequence))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        sequence = lines[0]
        return cls(ProblemInput(sequence))

    def solve(self) -> Literal["yes", "no"]:

        opened = {"(", "[", "{"}
        closed = {")": "(", "]": "[", "}": "{"}

        stack = []
        for char in self.sequence:
            if char in opened:
                stack.append(char)
            else:
                if stack and stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return "no"

        return "no" if stack else "yes"


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
