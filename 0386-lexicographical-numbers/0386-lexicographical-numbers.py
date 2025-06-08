class Solution(object):
    def lexicalOrder(self, n):
        output = []
        curr = 1

        for i in range(n):
            output.append(curr)
            if curr*10 <= n:
                curr *= 10
            else:
                while curr%10 == 9 or curr+1 > n:
                    curr //= 10
                curr += 1
        return output
        