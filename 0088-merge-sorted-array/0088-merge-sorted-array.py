class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mElement = m - 1
        nElement = n - 1 
        rightPos = m + n - 1

        while nElement >= 0:
            if mElement >= 0 and nums1[mElement] > nums2[nElement]:
                nums1[rightPos] = nums1[mElement]
                mElement -= 1
            else:
                nums1[rightPos] = nums2[nElement]
                nElement -= 1

            rightPos -= 1