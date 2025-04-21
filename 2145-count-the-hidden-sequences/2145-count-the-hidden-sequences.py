class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        lowerBound = (K:=list(accumulate(differences, initial=0)))
        upperBound = max(0, upper-lower+1-max(K)+min(K))
        return  upperBound and lowerBound 