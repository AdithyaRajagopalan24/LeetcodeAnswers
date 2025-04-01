class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [p.copy() for p in iterate_lexicographically(nums)]

def iterate_lexicographically(perm):
    n, perm = len(perm), sorted(perm)
    while True:
        yield perm
        for i in range(n-2, -1, -1):
            if perm[i] < perm[i+1]:
                for j in range(n-1, i, -1):
                    if perm[j] > perm[i]:
                        swap(perm, i, j)
                        break
                reverse(perm, i+1, n-1)
                break
        else:
            break
    
def swap(perm, i, j):
    perm[i], perm[j] = perm[j], perm[i]

def reverse(perm, i, j):
    while i < j:
        swap(perm, i, j)
        i += 1
        j -= 1