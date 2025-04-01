class Solution:
    def countAndSay(self, n: int) -> str:
    
        def process(s):
            ret = []
            stack = []
            for i in s:
                if stack and i != stack[-1]:
                    prev = stack[-1]
                    count = 0
                    while stack and stack[-1] == prev:
                        stack.pop()
                        count+=1
                    ret.append(str(count))
                    ret.append(prev)
                    stack.append(i)
                else:
                    stack.append(i)
            if stack:
                ret.append(str(len(stack)))
                ret.append(stack[-1])
            return "".join(ret)
        
        curr = "1"
        for i in range(2, n+1):
            curr = process(curr)
        return curr

            
            

        