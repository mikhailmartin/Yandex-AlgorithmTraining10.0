"""
Карточная игра

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В карточной игре колода раздаётся поровну двум игрокам. Далее они вскрывают по
одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты,
которые кладутся под низ его колоды. Тот, кто остаётся без карт – проигрывает.

Для простоты будем считать, что все карты различны по номиналу, а также, что
самая младшая карта побеждает самую старшую карту ("шестерка берёт туза").

Игрок, который забирает себе карты, сначала кладёт под низ своей колоды карту
первого игрока, затем карту второго игрока (то есть карта второго игрока
оказывается внизу колоды). Напишите программу, которая моделирует игру и
определяет, кто выигрывает. В игре участвует 10 карт, имеющих значения от 0 до 9,
большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.


Формат ввода:
Программа получает на вход две строки: первая строка содержит 5 чисел,
разделённых пробелами — номера карт первого игрока, вторая – аналогично 5 карт
второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается
с той карты, которая будет открыта первой.


Формат вывода:
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово
first или second, после чего вывести количество ходов, сделанных до выигрыша.
Если на протяжении 10^6 ходов игра не заканчивается, программа должна вывести
слово botva.


Пример 1
input: 1 3 5 7 9
input: 2 4 6 8 0
output: second 5

Пример 2
input: 2 4 6 8 0
input: 1 3 5 7 9
output: first 5

Пример 3
input: 1 7 3 9 4
input: 5 8 0 2 6
output: second 23
"""
from collections import deque
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    cards1: list[int]
    cards2: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        cards1 = list(map(int, input().split()))
        cards2 = list(map(int, input().split()))
        return cls(ProblemInput(cards1, cards2))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        cards1 = list(map(int, lines[0].split()))
        cards2 = list(map(int, lines[1].split()))
        return cls(ProblemInput(cards1, cards2))

    def solve(self) -> str:

        cards1 = deque(self.data.cards1)
        cards2 = deque(self.data.cards2)

        stop = 10 ** 6
        i = 0
        while i < stop and cards1 and cards2:
            card1 = cards1.popleft()
            card2 = cards2.popleft()
            if card1 == 0 and card2 == 9:
                cards1.extend([card1, card2])
            elif card2 == 0 and card1 == 9:
                cards2.extend([card1, card2])
            elif card1 > card2:
                cards1.extend([card1, card2])
            else:
                cards2.extend([card1, card2])
            i += 1

        if not cards1:
            return f"second {i}"
        elif not cards2:
            return f"first {i}"
        else:
            return "botva"


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
