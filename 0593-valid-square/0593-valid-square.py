class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        complexPts = [complex(*p) for p in sorted([p1, p2, p3, p4])]
        diag1 = complexPts[3] - complexPts[0]
        diag2 = complexPts[2] - complexPts[1]
        if (abs(diag1) == abs(diag2) > 0 and diag1.real * diag2.real + diag1.imag * diag2.imag == 0 and (complexPts[0] + complexPts[3])/2 == (complexPts[1] + complexPts[2])/2):
            return True
        return False
        # mp1 = list([p1[0] - p3[0], p1[1] - p3[1]])
        # mp2 = list([p2[0] - p4[0], p2[1] - p4[1]])
        # if mp1 == mp2:
        #     if mp2[0]**2 + mp2[1]**2 == mp1[1]**2 + mp1[0]**2:
        #         if mp1[0]*mp2[0] == mp1[1]*mp2[1]:
        #             return True
        # return False
