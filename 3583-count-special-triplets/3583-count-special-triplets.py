class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        pairCountMap = {}
        freqMap = {}
        totalTriplets = 0
        for value in nums:
            if value in pairCountMap:
                totalTriplets = (totalTriplets + pairCountMap[value]) % MOD
            doubled = value * 2
            if doubled in freqMap:
                pairCountMap[doubled] = (pairCountMap.get(doubled, 0) + freqMap[doubled]) % MOD
            freqMap[value] = freqMap.get(value, 0) + 1
        return totalTriplets