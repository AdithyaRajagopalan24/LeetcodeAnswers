class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        positions = [0] * n

        for i in range(n):
            positions[nums2[i]] = i
        nums1 = [positions[x] for x in nums1]

        firstBit = [0] * (n + 2)
        secondBit = [0] * (n + 2)

        def update(bit, i, val):
            i += 1
            while i <= n:
                bit[i] += val
                i += i & -i

        def query(bit, i):
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        finalCount = 0
        for i in reversed(range(n)):
            x = nums1[i]
            val = query(firstBit, n - 1) - query(firstBit, x)
            tripletsPossible = query(secondBit, n - 1) - query(secondBit, x)
            finalCount += tripletsPossible
            update(secondBit, x, val)
            update(firstBit, x, 1)

        return finalCount