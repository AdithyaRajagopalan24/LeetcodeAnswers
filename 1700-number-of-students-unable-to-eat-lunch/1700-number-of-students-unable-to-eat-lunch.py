class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        want0 = students.count(0)
        want1 = len(students) - want0
        for s in sandwiches:
            if s == 0:
                if want0 == 0:
                    return want1
                want0 -= 1
            else:
                if want1 == 0:
                    return want0
                want1 -= 1
        return 0