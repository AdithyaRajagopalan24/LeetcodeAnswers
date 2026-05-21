class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dpArray = [1] * len(nums)
        longestLength = 1

        for currentIndex in range(1, len(nums)):
            for previousIndex in range(currentIndex):
                if nums[currentIndex] > nums[previousIndex]:
                    dpArray[currentIndex] = max(
                        dpArray[currentIndex],
                        dpArray[previousIndex] + 1
                    )

            if dpArray[currentIndex] > longestLength:
                longestLength = dpArray[currentIndex]

        return longestLength