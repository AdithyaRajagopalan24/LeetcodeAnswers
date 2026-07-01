class Solution:
    def hoursNeeded(self, bananas, rate):
        timeSpent = 0

        for amount in bananas:
            quotient, remainder = divmod(amount, rate)
            timeSpent += quotient
            if remainder:
                timeSpent += 1

        return timeSpent

    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            guess = (low + high) // 2

            if self.hoursNeeded(piles, guess) > h:
                low = guess + 1
            else:
                high = guess

        return low