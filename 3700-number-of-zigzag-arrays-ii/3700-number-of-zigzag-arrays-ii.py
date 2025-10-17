class Solution:
    def matMul(self, a, b):
        n, m, p = len(a), len(b), len(b[0])
        res = [[0] * p for _ in range(n)]
        mod = 10**9 + 7
        for i in range(n):
            for k in range(m):
                if a[i][k]:
                    for j in range(p):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % mod
        return res

    def matPow(self, mat, exp):
        n = len(mat)
        res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while exp:
            if exp & 1:
                res = self.matMul(res, mat)
            mat = self.matMul(mat, mat)
            exp >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        size = 2 * m
        trans = [[0] * size for _ in range(size)]
        for x in range(m):
            for y in range(m):
                if y > x:
                    trans[x][m + y] = 1
                if y < x:
                    trans[m + x][y] = 1
        vec = [[1] for _ in range(size)]
        transExp = self.matPow(trans, n - 1)
        res = self.matMul(transExp, vec)
        return sum(row[0] for row in res) % (10**9 + 7)
