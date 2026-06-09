class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0

        for num in range(num1, num2 + 1):
            digits = []

            while num:
                digits.append(num % 10)
                num //= 10

                if len(digits) < 3:
                    continue

                a, b, c = digits[-3:]

                if (b < a and b < c) or (b > a and b > c):
                    total += 1

        return total