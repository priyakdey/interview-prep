# https://leetcode.com/problems/implement-queue-using-stacks/


class Stack:
    def __init__(self) -> None:
        self.__data = []

    def push(self, element: int) -> None:
        self.__data.append(element)

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Empty stack.... !")
        return self.__data.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise Exception("Empty stack.... !")
        return self.__data[-1]

    def is_empty(self) -> None:
        return len(self.__data) == 0


class MyQueue:
    def __init__(self):
        self.__active = Stack()
        self.__helper = Stack()

    def push(self, x: int) -> None:
        self.__active.push(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception("Empty Queue")

        # swap from active to helper
        self.__swap(self.__active, self.__helper)
        x = self.__helper.pop()
        # swap from helper to active
        self.__swap(self.__helper, self.__active)
        return x

    def peek(self) -> int:
        if self.empty():
            raise Exception("Empty Queue")

        # swap from active to helper
        self.__swap(self.__active, self.__helper)
        x = self.__helper.peek()
        # swap from helper to active
        self.__swap(self.__helper, self.__active)
        return x

    def empty(self) -> bool:
        return self.__active.is_empty()

    def __swap(self, _from: Stack, _to: Stack) -> None:
        while not _from.is_empty():
            _to.push(_from.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
