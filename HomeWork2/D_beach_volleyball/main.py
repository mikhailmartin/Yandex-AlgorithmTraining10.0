import sys
from collections import deque


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    teams = list(map(int, lines[1].split()))
    q = int(lines[2])
    k = [int(lines[i+3]) for i in range(q)]

    teams = deque(teams)
    k = [(idx, t) for idx, t in enumerate(k)]
    k = deque(sorted(k, key=lambda x: x[1]))
    res = [(-1, -1)] * q

    strongest = max(teams)
    strongest_pos = teams.index(strongest)

    for time in range(1, strongest_pos + 1):
        team1 = teams.popleft()
        team2 = teams.popleft()

        while k and k[0][1] == time:
            idx, t = k.popleft()
            res[idx] = (team1, team2)

        if team1 > team2:
            teams.appendleft(team1)
            teams.append(team2)
        else:
            teams.appendleft(team2)
            teams.append(team1)

    teams = list(teams)
    period = n - 1
    while k:
        idx, t = k.popleft()
        pos = (t - (strongest_pos + 1)) % period + 1
        res[idx] = (teams[0], teams[pos])

    return res


if __name__ == "__main__":
    result = main()
    for answer in result:
        print(*answer)
