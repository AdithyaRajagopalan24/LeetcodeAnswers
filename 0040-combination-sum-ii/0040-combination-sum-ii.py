class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, start, combination):
            if remain == 0:
                results.append(combination[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # Skip duplicates
                if candidates[i] > remain:
                    break  # Pruning
                
                combination.append(candidates[i])
                backtrack(remain - candidates[i], i + 1, combination)
                combination.pop()

        results = []
        candidates.sort()
        backtrack(target, 0, [])
        return results