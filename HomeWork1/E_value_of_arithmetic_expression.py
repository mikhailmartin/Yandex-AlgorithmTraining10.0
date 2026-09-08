"""
Значение арифметического выражения

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Задано числовое выражение. Необходимо вычислить его значение или установить, что
оно содержит ошибку. В выражении могут встречаться знаки сложения, вычитания,
умножения, скобки и пробелы (пробелов внутри чисел быть не должно). Приоритет
операций стандартный. Все числа в выражении целые и по модулю не превосходят
2×10^9. Также гарантируется, что все промежуточные вычисления также не
превосходят 2×10^9.


Формат ввода:
В первой строке вводится выражение. Его длина не превосходит 100 знаков. После
выражения идёт переход на новую строчку.


Формат вывода:
Выведите значение этого выражения или слово "WRONG", если значение не определено.


Пример 1
input: 1+(2*2 - 3)
output: 2

Пример 2
input: 1+a+1
output: WRONG

Пример 3
input: 1 1 + 2
output: WRONG
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    string: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        string = input()
        return cls(ProblemInput(string))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        string = lines[0]
        return cls(ProblemInput(string))

    def solve(self) -> int | str:

        infix = self._to_infix(self.data.string)
        try:
            self._validate(infix)
        except ValueError:
            return "WRONG"
        postfix = self._to_postfix(infix)

        stack = []
        for elem in postfix:
            if elem.isdigit():
                stack.append(int(elem))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if elem == "+":
                    stack.append(operand1 + operand2)
                elif elem == "-":
                    stack.append(operand1 - operand2)
                elif elem == "*":
                    stack.append(operand1 * operand2)

        return stack.pop()

    @staticmethod
    def _to_infix(string) -> list[str]:

        n = len(string)

        infix = []
        i = 0
        while i < n:
            if string[i] == " ":
                i += 1
            elif string[i].isdigit():
                num = []
                while i < n and string[i].isdigit():
                    num.append(string[i])
                    i += 1
                infix.append("".join(num))
            else:
                infix.append(string[i])
                i += 1

        return infix

    @staticmethod
    def _validate(infix: list[str]) -> None:

        operators = ("+", "-", "*")

        prev_elem = ""
        bracket_count = 0
        for elem in infix:
            if elem.isalpha():
                raise ValueError
            if elem.isdigit() and (prev_elem.isdigit() or prev_elem == ")"):
                raise ValueError
            if elem in operators and (prev_elem in operators or prev_elem == "("):
                raise ValueError
            if elem == "(":
                if prev_elem.isdigit() or prev_elem == ")":
                    raise ValueError
                bracket_count += 1
            if elem == ")":
                if prev_elem in operators or prev_elem == "(":
                    raise ValueError
                bracket_count -= 1
                if bracket_count < 0:
                    raise ValueError
            prev_elem = elem

        if infix[-1] in operators or infix[-1] == "(":
            raise ValueError

        if bracket_count != 0:
            raise ValueError
        if not (prev_elem.isdigit() or prev_elem == ")"):
            raise ValueError

    @staticmethod
    def _to_postfix(infix: list[str]) -> list[str]:

        postfix = []
        stack = []
        for elem in infix:
            if elem.isdigit():
                postfix.append(elem)
            elif elem in ("+", "-"):
                while stack and stack[-1] in ("+", "-", "*"):
                    postfix.append(stack.pop())
                stack.append(elem)
            elif elem == "*":
                while stack and stack[-1] == "*":
                    postfix.append(stack.pop())
                stack.append(elem)
            elif elem == "(":
                stack.append(elem)
            elif elem == ")":
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
