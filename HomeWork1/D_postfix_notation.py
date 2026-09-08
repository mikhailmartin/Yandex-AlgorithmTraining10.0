"""
Постфиксная запись

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В постфиксной записи (или обратной польской записи) операция записывается после
двух операндов. Например, сумма двух чисел A и B записывается как A B +.
Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * +
означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не
требует скобок и дополнительных соглашений о приоритете операторов для своего
чтения.


Формат ввода:
В единственной строке записано выражение в постфиксной записи, содержащее цифры
и операции +, -, *. Цифры и операции разделяются пробелами. В конце строки может
быть произвольное количество пробелов.


Формат вывода:
Необходимо вывести значение записанного выражения.


Пример
input: 8 9 + 1 7 - *
output: -102
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    postfix: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        postfix = input()
        return cls(ProblemInput(postfix))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        postfix = lines[0]
        return cls(ProblemInput(postfix))

    def solve(self) -> int:

        stack = []
        for elem in self.data.postfix.split():
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


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
