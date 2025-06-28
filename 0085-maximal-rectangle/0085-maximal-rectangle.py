class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:


        def histogram_area(arr:list[int])->int:

            stack,left,right,m=[],[],[],0

            for i in range(len(arr)):
                while stack and stack[-1][0]>=arr[i]:
                    stack.pop()
                if not stack:
                    left.append(-1)
                else:
                    left.append((stack[-1][1]))
                stack.append((arr[i],i))


            stack=[]


            for i in range(len(arr)-1,-1,-1):
                while stack and stack[-1][0]>=arr[i]:
                    stack.pop()
                if not stack:
                    right.append(len(arr))
                else:
                    right.append(stack[-1][1])
                stack.append((arr[i],i))
            right=right[::-1]


            for i in range(len(arr)):
                m=max(m,arr[i]*(right[i]-left[i]-1))


            return m


        buildings=[0]*len(matrix[0])
        maximal=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    buildings[j]+=1
                else:
                    buildings[j]=0
            cur=histogram_area(buildings)
            maximal=max(maximal,cur)
        return maximal
        