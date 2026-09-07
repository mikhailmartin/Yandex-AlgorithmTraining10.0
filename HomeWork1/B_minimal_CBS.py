"""
Минимальная ПСП

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Напомним определение правильной скобочной последовательности (ПСП):
- пустая строка — правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного типа —
правильная скобочная последовательность;
- правильная скобочная последовательность, к которой приписана слева или справа
правильная скобочная последовательность — тоже правильная скобочная
последовательность.

Пусть символы "[", "]", "(" и ")" некоторым образом упорядочены. Рассмотрим все
ПСП длины n состоящие из круглых и квадратных скобок и начинающиеся со строки s.
Среди этих ПСП необходимо найти лексикографически минимальную.

Строка A лексикографически меньше строки B (их длина совпадает), если существует
такое i, что для всех j < i A_j = B_j, а A_i < B_i.

Лексикографический порядок скобок задается строкой w, состоящей из 4 символов.
При этом w_1 < w_2 < w_3 < w_4. Например, если w = ()[], то (<)<[<].


Формат ввода:
В первой строке записано число n (1 ≤ n ≤ 100_000).
Во второй строке записана строка w, состоящая из 4 различных скобок.
В третьей строке записана строка s, ее длина не превосходит n.


Формат вывода:
Выведите ответ на задачу. Гарантируется что он существует.


Пример 1
input: 6
input: ()[]
input: ([(
output: ([()])

Пример 2
input: 6
input: ][)(
input: ([
output: ([][])

Пример 3
input: 4
input: (][)
input: ()[]
output: ()[]
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    w: str
    s: str


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def n(self) -> int:
        return self.data.n

    @property
    def w(self) -> str:
        return self.data.w

    @property
    def s(self) -> str:
        return self.data.s

    @classmethod
    def from_stdin(cls) -> Self:

        n = int(input())
        w = input()
        s = input()

        return cls(ProblemInput(n, w, s))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n = int(lines[0])
        w = lines[1]
        s = lines[2]

        return cls(ProblemInput(n, w, s))

    def solve(self) -> str:

        open_to_close = {"(": ")", "[": "]"}
        close_to_open = {")": "(", "]": "["}

        stack = []
        for char in self.s:
            if char in open_to_close:
                stack.append(char)
            elif stack and stack[-1] == close_to_open[char]:
                stack.pop()

        tail = []
        remain = self.n - len(self.s)
        while remain:
            if remain == len(stack):
                char = stack.pop()
                tail.append(open_to_close[char])
                remain -= 1
            else:
                for candidate in self.w:
                    if candidate in open_to_close:
                        tail.append(candidate)
                        stack.append(candidate)
                        remain -= 1
                    elif stack and candidate == open_to_close[stack[-1]]:
                        tail.append(candidate)
                        stack.pop()
                        remain -= 1
                    else:
                        continue
                    break

        return self.s + "".join(tail)


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
