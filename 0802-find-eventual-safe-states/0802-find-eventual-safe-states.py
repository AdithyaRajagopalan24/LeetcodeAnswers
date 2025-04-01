class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = set()
        ans = []

        def dfs(i: int) -> bool:
            if graph[i] == []:
                return True
            if i in seen:
                return False
            
            seen.add(i)
            for node in graph[i]:
                if not dfs(node):
                    return False
            
            # if it makes it here it traversed all neighbors and is good
            graph[i] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)

        return ans