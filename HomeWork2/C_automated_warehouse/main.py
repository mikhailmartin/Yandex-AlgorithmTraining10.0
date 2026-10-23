import sys
from collections import deque


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    a, b = map(int, lines[1].split())
    rovers = []
    for i in range(n):
        d, t = map(int, lines[i+2].split())
        rovers.append((d, t))

    a, b = min(a, b), max(a, b)
    res = [0] * n
    rovers = [(i, d, t) for i, (d, t) in enumerate(rovers)]
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
                    res[roads[a].popleft()] = time
                if roads[b]:
                    res[roads[b].popleft()] = time
            else:
                if roads[b - 1]:
                    res[roads[b - 1].popleft()] = time
                if roads[opposite[b - 1]]:
                    res[roads[opposite[b - 1]].popleft()] = time
        elif b == 4 and a == 1:
            if roads[b]:
                res[roads[b].popleft()] = time
            elif roads[a]:
                res[roads[a].popleft()] = time
            elif roads[opposite[b]]:
                res[roads[opposite[b]].popleft()] = time
            elif roads[opposite[a]]:
                res[roads[opposite[a]].popleft()] = time
        else:
            if roads[a]:
                res[roads[a].popleft()] = time
            elif roads[b]:
                res[roads[b].popleft()] = time
            elif roads[opposite[a]]:
                res[roads[opposite[a]].popleft()] = time
            elif roads[opposite[b]]:
                res[roads[opposite[b]].popleft()] = time

        time += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
