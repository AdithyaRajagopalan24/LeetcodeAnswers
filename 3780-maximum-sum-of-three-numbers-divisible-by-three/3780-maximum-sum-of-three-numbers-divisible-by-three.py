class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        top0 = [0, 0, 0]
        top1 = [0, 0, 0]
        top2 = [0, 0, 0]

        def insertTop(top, num):
            if num > top[0]:
                top[0] = num
                top.sort()

        for num in nums:
            r = num % 3
            if r == 0:
                insertTop(top0, num)
            elif r == 1:
                insertTop(top1, num)
            else:
                insertTop(top2, num)

        candidates = []
        if top0[2] and top1[2] and top2[2]:
            candidates.append(top0[2] + top1[2] + top2[2])
        if top0[0]:
            candidates.append(sum(top0))
        if top1[0]:
            candidates.append(sum(top1))
        if top2[0]:
            candidates.append(sum(top2))

        return max(candidates) if candidates else 0
