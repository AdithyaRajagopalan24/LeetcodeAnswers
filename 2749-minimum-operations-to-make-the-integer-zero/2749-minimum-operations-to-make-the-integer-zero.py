class Solution:
    def makeTheIntegerZero(self, value: int, decrement: int) -> int:
        remaining, steps = value, 1
        while True:
            remaining -= decrement
            if remaining < steps:
                return -1
            if steps >= remaining.bit_count():
                return steps
            steps += 1
        return -1
