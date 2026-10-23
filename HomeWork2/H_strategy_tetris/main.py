import sys
import heapq


def main(lines: list[str] | None = None) -> tuple[int, list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, W = map(int, lines[0].split())
    figures = []
    for i in range(n):
        a, w = map(int, lines[i+1].split())
        figures.append((a, w))

    figures = sorted((a, w, idx) for idx, (a, w) in enumerate(figures, 1))
    # здесь будем хранить (right, [figures], level)
    min_right = [(figures[0][0] + figures[0][1] - 1, [figures[0][2]], 1)]

    max_level = 1
    for i in range(1, n):
        a, w, idx = figures[i]

        right, figs, level = min_right[0]

        if a > right:
            heapq.heappop(min_right)
            figs.append(idx)
            heapq.heappush(min_right, (a + w - 1, figs, level))
        else:
            max_level += 1
            heapq.heappush(min_right, (a + w - 1, [idx], max_level))

    que = []
    max_level = -1
    for _, figs, level in min_right:
        que.extend(figs)
        max_level = max(max_level, level)

    return max_level, que


if __name__ == "__main__":
    result = main()
    print(result[0])
    print(*result[1])
