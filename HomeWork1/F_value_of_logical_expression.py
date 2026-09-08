"""
Значение логического выражения

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Задано логическое выражение. Необходимо вычислить его значение. В выражении
могут встречаться знаки ! (отрицание), & (логическое «и»), | (логическое «или»),
^ (XOR — «исключающее ИЛИ», «ровно одно из двух — истина») и скобки. Самый
высокий приоритет у отрицания, меньше – у &, операции | и ^ имеют самый низкий
приоритет (одинаковый) и вычисляются слева направо. Все числа в выражении
либо 0, либо 1.


Формат ввода:
В первой строке вводится выражение. Его длина не превосходит 100 знаков. После
выражения идёт переход на новую строчку.


Формат вывода:
Выведите значение этого выражения (0 или 1).


Пример
input: 1|(0&0^1)
output: 1
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    infix: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        infix = input()
        return cls(ProblemInput(infix))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        infix = lines[0]
        return cls(ProblemInput(infix))

    def solve(self) -> int:

        postfix = self._to_postfix(self.data.infix)

        stack = []
        for elem in postfix:
            if elem.isdigit():
                stack.append(bool(int(elem)))
            elif elem == "!":
                operand = stack.pop()
                stack.append(not operand)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if elem == "|":
                    stack.append(operand1 | operand2)
                elif elem == "^":
                    stack.append(operand1 ^ operand2)
                elif elem == "&":
                    stack.append(operand1 & operand2)

        return 1 if stack.pop() else 0

    @staticmethod
    def _to_postfix(infix: str) -> list[str]:

        postfix = []
        stack = []
        for char in infix:
            if char.isdigit():
                postfix.append(char)
            elif char in ("|", "^"):
                while stack and stack[-1] in ("|", "^", "&", "!"):
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == "&":
                while stack and stack[-1] in ("&", "!"):
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == "!":
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()

        while stack:
            postfix.append(stack.pop())

        return postfix


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
