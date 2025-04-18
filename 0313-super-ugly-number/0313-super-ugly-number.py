class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        superUglyNum = [1]
        primesCount = len(primes)
        indices = [0] * primesCount
        next = primes.copy()
        for i in range(1, n):
            superUglyNum.append(ugly := min(next))
            for k in range(primesCount):
                if ugly == next[k]:
                    indices[k] += 1
                    next[k] = primes[k] * superUglyNum[indices[k]]
        return superUglyNum[n - 1]