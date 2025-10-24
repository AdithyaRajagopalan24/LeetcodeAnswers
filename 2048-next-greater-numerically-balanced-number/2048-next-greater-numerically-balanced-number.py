class Solution:
    def nextBeautifulNumber(self, num: int) -> int:
        validNums = set()
        
        def build(idx, chosen):
            if idx == 8:
                if not chosen:
                    return
                seq = "".join(str(x) * x for x in chosen)
                if len(seq) <= 7:
                    for perm in set(permutations(seq)):
                        validNums.add(int("".join(perm)))
                else:
                    validNums.add(int("".join(sorted(seq))))
                return
            
            build(idx + 1, chosen)
            build(idx + 1, chosen + [idx])
        
        build(1, [])
        sortedNums = sorted(validNums)
        pos = bisect_right(sortedNums, num)
        return sortedNums[pos]
