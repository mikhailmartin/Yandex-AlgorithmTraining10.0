import sys
from collections import deque


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    cards1 = list(map(int, lines[0].split()))
    cards2 = list(map(int, lines[1].split()))

    cards1 = deque(cards1)
    cards2 = deque(cards2)

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


if __name__ == "__main__":
    result = main()
    print(result)
