class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        memoizationCache = {}

        def generateSubTrees(startValue, endValue):
            if (startValue, endValue) in memoizationCache:
                return memoizationCache[(startValue, endValue)]
            
            uniqueTrees = []
            if startValue > endValue:
                uniqueTrees.append(None)
                return uniqueTrees
            
            for rootValue in range(startValue, endValue + 1):
                leftSubTrees = generateSubTrees(startValue, rootValue - 1)
                rightSubTrees = generateSubTrees(rootValue + 1, endValue)
            
                for leftTree in leftSubTrees:
                    for rightTree in rightSubTrees:
                        currentRoot = TreeNode(rootValue, leftTree, rightTree)
                        uniqueTrees.append(currentRoot)
            
            memoizationCache[(startValue, endValue)] = uniqueTrees
            return uniqueTrees

        return generateSubTrees(1, n)