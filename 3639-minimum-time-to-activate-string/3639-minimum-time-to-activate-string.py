class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        totalSubs = int((n + 1) * (n / 2))
        if k > totalSubs:
            return -1

        def comboCount(x):
            return int((x + 1) * (x / 2))

        def validCount(t):
            temp = list(s)
            for i in range(t + 1):
                temp[order[i]] = '*'
            invalid = 0
            streak = 0
            for ch in temp:
                if ch == '*':
                    invalid += comboCount(streak)
                    streak = 0
                else:
                    streak += 1
            invalid += comboCount(streak)
            return totalSubs - invalid

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            count = validCount(mid)
            if count == k:
                return mid
            elif count >= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
