"""
Автоматизированный склад

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Склад представляет собой набор одинаковых квадратов, вокруг которых расположены
проезды. В углах каждого из квадратов расположены перекрёстки, образованные из
пересекающихся под прямым углом проездов.

По складу движутся роверы и при проезде перекрёстков они руководствуются
следующими правилами:
- На перекрёстке неравнозначных дорог ровер, движущийся по второстепенной
  дороге, должен уступить дорогу роверу, приближающимся по главной.
- Если главная дорога на перекрёстке меняет направление, роверы, движущиеся по
  главной дороге, должны руководствоваться между собой правилами проезда
  перекрёстков равнозначных дорог.
- На перекрёстке равнозначных дорог ровер обязан уступить дорогу транспортным
  средствам, приближающимся справа.

Для тестирования был выбран перекрёсток, для которого необходимо определить,
в каком порядке его проедут N роверов, подъезжающих к перекрёстку с каждой из
четырёх сторон в заданные моменты времени. Стороны обозначены номерами 1, 2, 3 и 4,
если перечислять по часовой стрелке. Известно, что за единицу времени с каждой
из сторон перекрёстка приезжает не более одного ровера, а все роверы соблюдают
правила и не обгоняют друг-друга. Поскольку это только начало тестирования, все
роверы хотят проехать перекрёсток прямо. Роверы, приближающиеся со сторон a и b
находятся на главной дороге, остальные — на второстепенной. На проезд
перекрёстка ровер тратит одну единицу времени.

Таким образом, ровер проезжает перекрёсток только если:
- нет роверов, которые находятся перед этим ровером в очереди к перекрёстку,
- нет роверов, которым нужно уступить дорогу.

Если два ровера, стоящие первыми в очереди на проезд перекрёстка не должны
уступать друг другу дорогу, то они проедут перекрёсток одновременно.

Определите, в каком порядке роверы проедут перекрёсток.


Формат ввода:
Первая строка входного файла содержит одно целое число N (1 ≤ N ≤ 100) —
количество роверов. Вторая строка содержит числа a и b — стороны перекрёстка,
составляющие главную дорогу (1 ≤ a, b ≤ 4, a ≠ b).

Каждая из следующих N строк содержит описание ровера, состоящее из двух целых
чисел d_i и t_i (1 ≤ d_i ≤ 4, 1 ≤ t_i ≤ 100) — направление и время приезда
i-ого ровера.


Формат вывода:
В выходной файл выведите N целых чисел по одному на строке. i-ая строка должна
содержать время, в которое i-ый ровер проедет перекрёсток.

Роверы занумерованы в порядке появления во входном файле.


Пример 1
input: 4
input: 1 3
input: 1 1
input: 3 1
input: 2 1
input: 2 2
output: 1
output: 1
output: 2
output: 3

Пример 2
input: 4
input: 1 2
input: 1 1
input: 2 1
input: 3 1
input: 4 1
output: 1
output: 2
output: 3
output: 4

Пример 3
input: 1
input: 1 4
input: 1 1
output: 1
"""
from collections import deque
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    a: int
    b: int
    rovers: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        a, b = map(int, input().split())
        rovers = []
        for _ in range(n):
           d, t = map(int, input().split())
           rovers.append((d, t))
        return cls(ProblemInput(n, a, b, rovers))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        a, b = map(int, lines[1].split())
        rovers = []
        for i in range(n):
            d, t = map(int, lines[i+2].split())
            rovers.append((d, t))
        return cls(ProblemInput(n, a, b, rovers))

    def solve(self) -> list[int]:

        a, b = min(self.data.a, self.data.b), max(self.data.a, self.data.b)
        result = [0] * self.data.n
        rovers = [(i, d, t) for i, (d, t) in enumerate(self.data.rovers)]
        rovers = deque(sorted(rovers, key=lambda x: x[2]))
        opposite = {1: 3, 2: 4, 3: 1, 4: 2}

        time = 0
        roads = [deque() for _ in range(5)]
        while rovers or any(roads):
            # роверы приезжают на перекрёсток
            while rovers and rovers[0][2] == time:
                i, d, t = rovers.popleft()
                roads[d].append(i)

            # ПРАВИЛА РАЗЪЕЗДОВ
            if a == opposite[b]:
                if roads[a] or roads[b]:
                    if roads[a]:
                        result[roads[a].popleft()] = time
                    if roads[b]:
                        result[roads[b].popleft()] = time
                else:
                    if roads[b-1]:
                        result[roads[b-1].popleft()] = time
                    if roads[opposite[b-1]]:
                        result[roads[opposite[b-1]].popleft()] = time
            elif b == 4 and a == 1:
                if roads[b]:
                    result[roads[b].popleft()] = time
                elif roads[a]:
                    result[roads[a].popleft()] = time
                elif roads[opposite[b]]:
                    result[roads[opposite[b]].popleft()] = time
                elif roads[opposite[a]]:
                    result[roads[opposite[a]].popleft()] = time
            else:
                if roads[a]:
                    result[roads[a].popleft()] = time
                elif roads[b]:
                    result[roads[b].popleft()] = time
                elif roads[opposite[a]]:
                    result[roads[opposite[a]].popleft()] = time
                elif roads[opposite[b]]:
                    result[roads[opposite[b]].popleft()] = time

            time += 1

        return result


def main():

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
