class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev = 0

        for log in logs:
            fid, typ, t = log.split(':')
            fid = int(fid)
            t = int(t)

            if typ == "start":
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(fid)
                prev = t
            else:
                res[stack.pop()] += t - prev + 1
                prev = t + 1
        return res