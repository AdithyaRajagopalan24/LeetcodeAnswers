class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr = nums
        max_value = max(arr)
        counts = [0] * (max_value + 1)
        for n in arr:
            counts[n] += 1
        i = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                arr[i] = n
                i += 1
        print(arr)