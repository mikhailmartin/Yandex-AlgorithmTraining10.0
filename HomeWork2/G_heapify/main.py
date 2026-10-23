import sys


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
        res = self._heap.pop()

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

        return res

    @property
    def size(self) -> int:
        return len(self._heap)


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    res = []
    heap = Heap()
    for i in range(n):
        command = lines[i+1]
        if command.startswith("0"):
            _, operand = command.split()
            operand = int(operand)
            heap.insert(operand)
        else:
            res.append(heap.extract())

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
