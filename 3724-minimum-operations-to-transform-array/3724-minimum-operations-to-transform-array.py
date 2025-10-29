class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        finalTarget = nums2[-1]
        totalOps = 0
        minAdjust = math.inf
        for i in range(len(nums2) - 1):
            if (nums1[i] < finalTarget < nums2[i]) or (nums2[i] < finalTarget < nums1[i]):
                minAdjust = 0
            distanceToTarget = min(abs(finalTarget - nums1[i]), abs(finalTarget - nums2[i]))
            minAdjust = min(minAdjust, distanceToTarget)
            totalOps += abs(nums1[i] - nums2[i])
        return totalOps + minAdjust + 1
