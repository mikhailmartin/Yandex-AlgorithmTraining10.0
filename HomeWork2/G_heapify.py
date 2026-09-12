"""
Хипуй

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В этой задаче вам необходимо самостоятельно (не используя соответствующие
классы и функции стандартной библиотеки) организовать структуру данных Heap для
хранения целых чисел, над которой определены следующие операции:
a) Insert(k) — добавить в Heap число k;
b) Extract — достать из Heap наибольшее число (удалив его при этом).


Формат ввода:
В первой строке содержится количество команд N (1 ≤ N ≤ 100_000), далее следуют
N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или
“1”, обозначающий, соответственно, операции Insert(<число>) и Extract.
Гарантируется, что при выполнении команды Extract в структуре находится по
крайней мере один элемент.


Формат вывода:
Для каждой команды извлечения необходимо отдельной строкой вывести число,
полученное при выполнении команды Extract.


Пример 1
input: 2
input: 0 10000
input: 1
output: 10000

Пример 2
input: 14
input: 0 1
input: 0 345
input: 1
input: 0 4346
input: 1
input: 0 2435
input: 1
input: 0 235
input: 0 5
input: 0 365
input: 1
input: 1
input: 1
input: 1
output: 345
output: 4346
output: 2435
output: 365
output: 235
output: 5
output: 1
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    commands: list[str]


class Heap:
    def __init__(self) -> None:
        self._heap = []

    def __getitem__(self, item: int) -> int:
        return self._heap[item]

    def __setitem__(self, key: int, value: int) -> None:
        self._heap[key] = value

    def insert(self, num: int) -> None:
        self._heap.append(num)
        i = self.size - 1
        while i and self[(i - 1) // 2] < self[i]:
            self[(i - 1) // 2], self[i] = self[i], self[(i - 1) // 2]
            i = (i - 1) // 2

    def extract(self) -> int:

        self[0], self[self.size - 1] = self[self.size - 1], self[0]
        result = self._heap.pop()

        i = 0
        while True:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            if left_i > self.size - 1:
                break
            elif right_i > self.size - 1:
                child_i = left_i
            elif self[left_i] > self[right_i]:
                child_i = left_i
            else:
                child_i = right_i

            if self[i] < self[child_i]:
                self[i], self[child_i] = self[child_i], self[i]
                i = child_i
            else:
                break

        return result

    @property
    def size(self) -> int:
        return len(self._heap)

class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        commands = []
        for _ in range(n):
            command = input()
            commands.append(command)
        return cls(ProblemInput(n, commands))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        commands = []
        for i in range(n):
            command = lines[i+1]
            commands.append(command)
        return cls(ProblemInput(n, commands))

    def solve(self) -> list[int]:

        result = []
        heap = Heap()
        for command in self.data.commands:
            if command.startswith("0"):
                _, operand = command.split()
                operand = int(operand)
                heap.insert(operand)
            else:
                result.append(heap.extract())

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)


if __name__ == "__main__":
    main()
