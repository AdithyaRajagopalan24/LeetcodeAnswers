class Solution:
    def addOperators(self, digits: str, target: int) -> List[str]:
        results = []

        def dfs(index, expr, total, lastVal):
            if index == len(digits):
                if total == target:
                    results.append(expr)
                return

            for j in range(index, len(digits)):
                if j > index and digits[index] == '0':
                    break
                val = int(digits[index:j+1])
                if index == 0:
                    dfs(j+1, str(val), val, val)
                else:
                    dfs(j+1, expr + "+" + str(val), total + val, val)
                    dfs(j+1, expr + "-" + str(val), total - val, -val)
                    dfs(j+1, expr + "*" + str(val), total - lastVal + lastVal * val, lastVal * val)

        dfs(0, "", 0, 0)
        return results
