class Solution:
    def lastInteger(self, n: int) -> int:
        def operation1(left, right, step):
            if left == right:
                return left
            middle = left + step
            if (right - middle) % (step * 2) == 0:
                newRight = right - step
            else:
                newRight = right
            return operation2(left, newRight, step * 2)

        def operation2(left, right, step):
            if left == right:
                return left
            middle = right - step
            if (middle - left) % (step * 2) == 0:
                newLeft = left + step
            else:
                newLeft = left
            return operation1(newLeft, right, step * 2)

        return operation1(1, n, 1)
