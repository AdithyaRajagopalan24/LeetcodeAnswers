class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        stringNums = list(map(str, nums))
        stringNums.sort(key=lambda value: value * 10, reverse=True)
        if stringNums[0] == "0":
            return "0"
        largestNumber = "".join(stringNums)
        return largestNumber