from typing import List
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = [0] * (n - k + 1)
        freq = {}
        chosen = set()
        top = []
        rest = []
        total = 0

        def clean():
            while top and (top[0][1] not in chosen or freq.get(top[0][1], 0) != top[0][0]):
                heapq.heappop(top)
            while rest and ((-rest[0][1]) in chosen or freq.get(-rest[0][1], 0) != -rest[0][0] or -rest[0][0] == 0):
                heapq.heappop(rest)

        def demote(v: int):
            nonlocal total
            if v in chosen:
                chosen.remove(v)
                total -= v * freq.get(v, 0)

        def promote():
            nonlocal total
            clean()
            while len(chosen) < x and rest:
                f, v = -rest[0][0], -rest[0][1]
                if freq.get(v, 0) != f or v in chosen or f == 0:
                    heapq.heappop(rest)
                    continue
                heapq.heappop(rest)
                chosen.add(v)
                total += v * f
                heapq.heappush(top, (f, v))
            clean()

        def add(v: int):
            nonlocal total
            demote(v)
            f = freq.get(v, 0) + 1
            freq[v] = f
            heapq.heappush(rest, (-f, -v))
            if len(chosen) < x:
                promote()
            else:
                clean()
                if rest and top:
                    bf, bv = -rest[0][0], -rest[0][1]
                    wf, wv = top[0]
                    if bf > wf or (bf == wf and bv > wv):
                        heapq.heappop(rest)
                        chosen.add(bv)
                        total += bv * bf
                        heapq.heappush(top, (bf, bv))
                        heapq.heappop(top)
                        if wv in chosen:
                            chosen.remove(wv)
                            total -= wv * wf
                        heapq.heappush(rest, (-wf, -wv))
                clean()

        def remove(v: int):
            nonlocal total
            demote(v)
            f = freq.get(v, 0) - 1
            if f <= 0:
                freq.pop(v, None)
            else:
                freq[v] = f
                heapq.heappush(rest, (-f, -v))
            promote()

        for i in range(k):
            add(nums[i])
        res[0] = total

        for i in range(k, n):
            remove(nums[i - k])
            add(nums[i])
            res[i - k + 1] = total

        return res
