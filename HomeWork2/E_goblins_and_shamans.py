"""
Гоблины и шаманы

Ограничение времени - 1 секунда
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Гоблины Мглистых гор очень любях ходить к своим шаманам. Так как гоблинов много,
к шаманам часто образуются очень длинные очереди. А поскольку много гоблинов в
одном месте быстро образуют шумную толку, которая мешает шаманам проводить
сложные медицинские манипуляции, последние решили установить некоторые правила
касательно порядка в очереди.

Обычные гоблины при посещении шаманов должны вставать в конец очереди.
Привилегированные же гоблины, знающие особый пароль, встают ровно в её середину,
причём при нечётной длине очереди они встают сразу за центром.

Так как гоблины также широко известны своим непочтительным отношением ко
всяческим правилам и законам, шаманы попросили вас написать программу, которая
бы отслеживала порядок гоблинов в очереди.


Формат ввода:
В первой строке входных данный записано число N (1 ≤ N ≤ 10^5) — количество
запросов к программе. Следующие N строк содержат описание запросов в формате:
”+ i” — гоблин с номером i (1 ≤ i ≤ N) встаёт в конец очереди.
”* i” — привилегированный гоблин с номером i встаёт в середину очереди.
”-” — первый гоблин из очереди уходит к шаманам. Гарантируется, что на момент
такого запроса очередь не пуста.


Формат вывода:
Для каждого запроса типа ”-” программа должна вывести номер гоблина, который
должен зайти к шаманам.


Пример
input: 7
input: + 1
input: + 2
input: -
input: + 3
input: + 4
input: -
input: -
output: 1
output: 2
output: 3
"""
from collections import deque
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    queries: list[str]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        queries = []
        for _ in range(n):
           queries.append(input())
        return cls(ProblemInput(n, queries))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        queries = []
        for i in range(n):
            queries.append(lines[i+1])
        return cls(ProblemInput(n, queries))

    def solve(self) -> list[str]:

        left = deque()
        right = deque()
        result = []
        for query in self.data.queries:
            if query.startswith("+"):
                _, i = query.split()
                right.append(i)
                if len(left) < len(right):
                    left.append(right.popleft())
            elif query.startswith("*"):
                _, i = query.split()
                if len(left) == len(right):
                    left.append(i)
                else:
                    right.appendleft(i)
            elif query == "-":
                result.append(left.popleft())
                if len(left) < len(right):
                    left.append(right.popleft())

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(result))


if __name__ == "__main__":
    main()
