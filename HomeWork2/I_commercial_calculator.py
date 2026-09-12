"""
Коммерческий калькулятор

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Фирма OISAC выпустила новую версию калькулятора. Этот калькулятор берёт с
пользователя деньги за совершаемые арифметические операции. Стоимость каждой
операции в долларах равна 5% от числа, которое является результатом операции.
На этом калькуляторе требуется вычислить сумму N натуральных чисел (числа
известны). Нетрудно заметить, что от того, в каком порядке мы будем складывать
эти числа, иногда зависит, в какую сумму денег нам обойдётся вычисление суммы
чисел (тем самым оказывается нарушен классический принцип “от перестановки мест
слагаемых сумма не меняется”).

Например, пусть нам нужно сложить числа 10, 11, 12 и 13. Тогда если мы сначала
сложим 10 и 11 (это обойдётся нам в 1.05 €), потом результат с 12 (1.65 €), и
затем с 13 (2.3 €), то всего мы заплатим 5 €, если же сначала отдельно сложить
10 и 11 (1.05 €), потом 12 и 13 (1.25 €) и, наконец, сложить между собой два
полученных числа (2.3 €), то в итоге мы заплатим лишь 4.6 €. Напишите программу,
которая будет определять, за какую минимальную сумму денег можно найти сумму
данных N чисел.


Формат ввода:
Первая строка входных данных содержит число N (2 ≤ N ≤ 10^5). Во второй строке
заданы N натуральных чисел, каждое из которых не превосходит 10000.


Формат вывода:
Определите, сколько денег нам потребуется на нахождения суммы этих N чисел.
Результат должен быть выведен с двумя знаками после десятичной точки.


Пример 1
input: 4
input: 10 11 12 13
output: 4.60

Пример 2
input: 2
input: 1 1
output: 0.10
"""
import heapq
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    nums: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        nums = list(map(int, input().split()))
        return cls(ProblemInput(n, nums))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        nums = list(map(int, lines[1].split()))
        return cls(ProblemInput(n, nums))

    def solve(self) -> str:

        nums = self.data.nums

        cost = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            operand1 = heapq.heappop(nums)
            operand2 = heapq.heappop(nums)
            result = operand1 + operand2
            heapq.heappush(nums, result)
            cost += result * 0.05

        return f"{cost:.2f}"


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
