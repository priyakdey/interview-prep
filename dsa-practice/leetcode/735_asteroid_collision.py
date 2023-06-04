from typing import List, Tuple


class Stack:
    def __init__(self) -> None:
        self._table = []

    def pop(self) -> int:
        if len(self._table) == 0:
            raise Exception("Empty Stack")
        val = self._table[-1]
        del self._table[-1]
        return val

    def peek(self) -> int:
        if len(self._table) == 0:
            raise Exception("Empty Stack")
        return self._table[-1]

    def push(self, val: int) -> None:
        self._table.append(val)

    def is_empty(self) -> bool:
        return len(self._table) == 0

    def pos_neg_val_count(self) -> Tuple[int]:
        pos_count = 0
        for val in self._table:
            if val >= 0:
                pos_count += 1

        return (pos_count, len(self._table) - pos_count)


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack1 = Stack()  # pre-filled with list data at start
        stack2 = Stack()  # this is empty at start
        for num in asteroids:
            stack1.push(num)

        def collide(stack1: "Stack", stack2: "Stack") -> None:
            while not stack1.is_empty():
                val = stack1.pop()
                if stack2.is_empty():
                    stack2.push(val)
                else:
                    last_val = stack2.peek()
                    if (val >= 0 and last_val < 0) or (val < 0 and last_val >= 0):
                        # need to collide
                        if abs(val) > abs(last_val):
                            stack2.pop()
                            stack2.push(val)
                        if abs(val) == abs(last_val):
                            stack2.pop()
                    else:
                        stack2.push(val)

        active_stack = stack1  # stack which always holds the data after collision
        empty_stack = stack2  # stack which is always empty after collision

        can_collide = True
        while can_collide:
            collide(active_stack, empty_stack)

            # now empty stack has the data, swap the ref
            temp = active_stack
            active_stack = empty_stack
            empty_stack = temp

            (pos, neg) = active_stack.pos_neg_val_count()
            if active_stack.is_empty():
                can_collide = False
            elif pos == 0 or neg == 0:
                can_collide = False
            else:
                can_collide = True

        after_collision = []
        if not active_stack.is_empty():
            while not active_stack.is_empty():
                after_collision.append(active_stack.pop())

        return after_collision


soln = Solution()
# print(soln.asteroidCollision([5, 10, -5]))
# print(soln.asteroidCollision([8, -8]))
# print(soln.asteroidCollision([10, 2, -5]))
print(soln.asteroidCollision([-2, -1, 1, 2]))
