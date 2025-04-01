class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        while n != 1 and n not in checked:
            checked.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1