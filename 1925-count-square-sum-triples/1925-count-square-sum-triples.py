class Solution(object):
    def countTriples(self, n):
        squares = {i * i for i in range(1, n + 1)}
        totalTriples = 0
        
        for a in range(1, n + 1):
            a2 = a * a
            for b in range(a + 1, n + 1):
                s = a2 + b * b
                if s in squares:
                    totalTriples += 2
        
        return totalTriples
