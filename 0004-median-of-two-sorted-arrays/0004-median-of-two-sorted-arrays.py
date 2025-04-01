class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        minVal = min(nums1)
        maxVal = max(nums1)
        tagCount = maxVal - minVal + 1
        tags = [[] for i in range(tagCount)]
        for k in nums1:
            tags[k-minVal].append(k)
        finalArr = []
        for j in tags:
            finalArr.extend(j)
        print(finalArr)
        if len(finalArr)%2 == 0:
            return ((finalArr[int(len(finalArr)/2)] + finalArr[int((len(finalArr)/2) - 1)])/2)
        else:
            return (finalArr[int((len(finalArr)-1)/2)])
