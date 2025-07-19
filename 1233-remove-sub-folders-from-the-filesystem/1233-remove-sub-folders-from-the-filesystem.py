class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        s=set()
        ans=[]
        for i in sorted(folder,key=len):
            val=i[1:].split('/')
            for v in range(len(val)):
                if tuple(val[:v]) in s:
                    break
            else:
                ans.append(i)
                s.add(tuple(val))
        return ans