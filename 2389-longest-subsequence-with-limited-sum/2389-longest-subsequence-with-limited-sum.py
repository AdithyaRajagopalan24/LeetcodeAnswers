class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pref = list(accumulate(nums))
        ans = []
        for q in queries:
            maxseq = bisect_right(pref, q)
            ans.append(maxseq)