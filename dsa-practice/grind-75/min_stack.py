# https://leetcode.com/problems/min-stack/


from typing import Tuple


class MinStack:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.is_empty():
            self.data.append((val, val))
            self.size += 1
            return

        minn = self.__peek()[1]
        if val < minn:
            minn = val
        self.data.append((val, minn))
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Empty Stack")

        self.size -= 1
        return self.data.pop(-1)[0]

    def top(self) -> int:
        return self.__peek()[0]

    def getMin(self) -> int:
        return self.__peek()[1]

    def is_empty(self) -> bool:
        return self.size == 0

    def __peek(self) -> Tuple[int]:
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.data[-1]
