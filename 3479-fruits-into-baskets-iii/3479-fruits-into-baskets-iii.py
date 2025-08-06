class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1

        segTree = [0] * (2 * size)
        for i in range(n):
            segTree[size + i] = baskets[i]
        for i in range(size - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])

        def query(fruit):
            idx = 1
            if segTree[idx] < fruit:
                return -1
            while idx < size:
                if segTree[2 * idx] >= fruit:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx

        def update(idx):
            segTree[idx] = -1
            while idx > 1:
                idx //= 2
                segTree[idx] = max(segTree[2 * idx], segTree[2 * idx + 1])

        unplaced = 0
        for fruit in fruits:
            pos = query(fruit)
            if pos == -1:
                unplaced += 1
            else:
                update(pos)

        return unplaced
