import sys
from collections import deque


class Queue(deque):
    def push(self, num: str) -> str:
        self.append(num)
        return "ok"

    def pop(self) -> str:
        if self.size() == "0":
            return "error"
        return self.popleft()

    def front(self) -> str:
        if self.size() == "0":
            return "error"
        return self[0]

    def size(self) -> str:
        return str(len(self))

    def clear(self) -> str:
        super().clear()
        return "ok"


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    res = []
    i = 0
    queue = Queue()
    while True:
        command = lines[i]
        if command == "exit":
            res.append("bye")
            break
        elif command.startswith("push"):
            command, operand = command.split()
            res.append(queue.push(operand))
        elif command == "pop":
            res.append(queue.pop())
        elif command == "front":
            res.append(queue.front())
        elif command == "size":
            res.append(queue.size())
        elif command == "clear":
            res.append(queue.clear())
        i += 1

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
