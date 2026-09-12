"""
Strategy tetris

Ограничение времени - 2 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Как и в обычном тетрисе, поле в игре Strategy Tetris представляет собой «стакан»
шириной в W клеток (1 ≤ W ≤ 10^9) и бесконечной высоты. В этот стакан падают
сверху N фигурок (1 ≤ N ≤ 100000). i-я фигурка представляет собой прямоугольник
шириной в W_i клеток и высотой в одну клетку; самая левая клетка фигурки имеет
абсциссу a_i (1 ≤ a_i ≤ W – W_i + 1). Фигурки падают по обычным правилам: если
при падении фигурка хотя бы одной своей клеткой ложится на какую-либо уже
упавшую фигурку, то её движение прекращается.

В отличие от обычного тетриса, игрок не имеет возможности вращать фигурки или
смещать их по горизонтали в процессе падения — ещё бы, это пришлось бы делать
быстро и не было бы времени серьёзно подумать над стратегией. Единственное, что
он может — это выбрать порядок, в котором эти N фигурок упадут в стакан (каждая
по одному разу). Ваша задача — помочь ему выбрать такой порядок, при котором
высота образовавшейся в результате падения конструкции была бы как можно меньше
(в отличие от обычного тетриса, полностью заполненная фигурками горизонталь
никуда не исчезает).


Формат ввода:
В первой строке входного файла записаны числа N и W, а в последующих N строках —
пары чисел a_i и W_i.


Формат вывода:
Выведите в выходной файл минимальную возможную высоту конструкции, а затем
последовательность номеров фигурок, к этой высоте приводящую. Фигурки нумеруются
натуральными числами от 1 до N в том порядке, в котором они указаны во входных
данных. Если возможных вариантов несколько, выведите любой из них.


Пример
input: 3 4
input: 1 2
input: 2 2
input: 3 2
output: 2
output: 3 1 2
"""
import heapq
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    W: int
    figures: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, W = map(int, input().split())
        figures = []
        for _ in range(n):
            a, w = map(int, input().split())
            figures.append((a, w))
        return cls(ProblemInput(n, W, figures))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, W = map(int, lines[0].split())
        figures = []
        for i in range(n):
            a, w = map(int, lines[i+1].split())
            figures.append((a, w))
        return cls(ProblemInput(n, W, figures))

    def solve(self) -> tuple[int, list[int]]:

        figures = sorted((a, w, idx) for idx, (a, w) in enumerate(self.data.figures, 1))
        # здесь будем хранить (right, [figures], level)
        min_right = [(figures[0][0] + figures[0][1] - 1, [figures[0][2]], 1)]

        max_level = 1
        for i in range(1, self.data.n):
            a, w, idx = figures[i]

            right, figs, level = min_right[0]

            if a > right:
                heapq.heappop(min_right)
                figs.append(idx)
                heapq.heappush(min_right, (a+w-1, figs, level))
            else:
                max_level += 1
                heapq.heappush(min_right, (a+w-1, [idx], max_level))

        que = []
        max_level = -1
        for _, figs, level in min_right:
            que.extend(figs)
            max_level = max(max_level, level)

        return max_level, que


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result[0])
    print(*result[1])


if __name__ == "__main__":
    main()
