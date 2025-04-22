from math import isqrt
from collections import defaultdict
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def idealArrays(self, length: int, limit: int) -> int:

        def sievePrimes(upperBound):
            isPrime = [True] * (upperBound + 1)
            primeNumbers = []
            for candidate in range(2, upperBound + 1):
                if isPrime[candidate]:
                    primeNumbers.append(candidate)
                    for multiple in range(candidate * candidate, upperBound + 1, candidate):
                        isPrime[multiple] = False
            return primeNumbers

        def primeFactorTable(primeList, maxNum):
            factorTable = defaultdict(list)
            totalPrimes = len(primeList)

            for index, p in enumerate(primeList):
                factorTable[p] = [0] * totalPrimes
                factorTable[p][index] = 1

            for num in range(2, maxNum + 1):
                if num not in factorTable:
                    factorTable[num] = [0] * totalPrimes
                    for idx, prime in enumerate(primeList):
                        if num % prime == 0:
                            prevFactors = factorTable[num // prime]
                            factorTable[num] = prevFactors.copy()
                            factorTable[num][idx] += 1
                            break
            return factorTable

        @lru_cache(None)
        def binomialCoeff(n, k):
            if k == 0:
                return 1
            if k == 1:
                return n
            if k > n:
                return 0
            return (binomialCoeff(n - 1, k) + binomialCoeff(n - 1, k - 1)) % MOD

        allPrimes = sievePrimes(limit)
        exponentMap = primeFactorTable(allPrimes, limit)

        totalCount = 0
        for base in range(1, limit + 1):
            primeCounts = exponentMap[base]
            ways = 1
            for power in primeCounts:
                if power > 0:
                    ways *= binomialCoeff(power + length - 1, min(length - 1, power))
                    ways %= MOD
            totalCount = (totalCount + ways) % MOD

        return totalCount
