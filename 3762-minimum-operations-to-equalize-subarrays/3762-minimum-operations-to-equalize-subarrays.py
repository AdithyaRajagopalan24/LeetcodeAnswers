class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        bad = [0]
        pv = -1
        p = 0
        for x in nums:
            v = x % k
            p += (v != pv)
            bad.append(p)
            pv = v

        vals = [x // k for x in nums]
        sortedVals = sorted(list(set(vals)))
        rankMap = {v: i for i, v in enumerate(sortedVals, 1)}
        m = len(sortedVals)
        
        blockSize = max(1, n // int(len(queries)**0.5 or 1))
        sortedQueries = [(s // blockSize, t, s, i) for i, (s, t) in enumerate(queries)]
        sortedQueries.sort(key=lambda x: (x[0], x[1] if x[0] & 1 else -x[1]))

        cntBit = [0] * (m + 1)
        sumBit = [0] * (m + 1)
        currCnt = 0
        currSum = 0
        
        def update(i, delta):
            nonlocal currCnt, currSum
            v = vals[i]
            rank = rankMap[v]
            
            valDelta = delta * v
            currCnt += delta
            currSum += valDelta
            
            while rank <= m:
                sumBit[rank] += valDelta
                cntBit[rank] += delta
                rank += rank & -rank

        ans = [-1] * len(queries)
        l, r = 0, -1
        highestBit = 1 << (m.bit_length() - 1)

        for _, qEnd, qStart, qIdx in sortedQueries:
            if bad[qEnd + 1] - bad[qStart + 1]:
                continue
            
            while l > qStart:
                l -= 1
                update(l, 1)
            while r < qEnd:
                r += 1
                update(r, 1)
            while l < qStart:
                update(l, -1)
                l += 1
            while r > qEnd:
                update(r, -1)
                r -= 1
            
            idx = 0
            prefixCnt = 0
            prefixSum = 0
            mask = highestBit
            target = currCnt >> 1
            
            while mask:
                nextIdx = idx + mask
                if nextIdx <= m and prefixCnt + cntBit[nextIdx] <= target:
                    idx = nextIdx
                    prefixCnt += cntBit[idx]
                    prefixSum += sumBit[idx]
                mask >>= 1
            
            median = sortedVals[idx]
            
            sufSum = currSum - prefixSum
            sufCnt = currCnt - prefixCnt
            
            ans[qIdx] = (sufSum - median * sufCnt + median * prefixCnt - prefixSum)

        return ans
