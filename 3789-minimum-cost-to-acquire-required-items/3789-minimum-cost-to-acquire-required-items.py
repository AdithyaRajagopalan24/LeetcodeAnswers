class Solution:
    def minimumCost(self, costOne, costTwo, costBoth, numOne, numTwo):
        costIndividually = costOne * numOne + costTwo * numTwo
        costCombined = costBoth * max(numOne, numTwo)
        costPartialCombined = costBoth * min(numOne, numTwo) + (costOne if numOne > numTwo else costTwo) * abs(numOne - numTwo)
        return min(costIndividually, costCombined, costPartialCombined)