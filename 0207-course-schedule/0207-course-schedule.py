class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = [[] for _ in range(numCourses)]
        courseIndegree = [0] * numCourses
        completedCourses = []

        for course, prereq in prerequisites:
            courseGraph[prereq].append(course)
            courseIndegree[course] += 1

        readyCourses = deque()
        for courseId in range(numCourses):
            if courseIndegree[courseId] == 0:
                readyCourses.append(courseId)

        while readyCourses:
            currentCourse = readyCourses.popleft()
            completedCourses.append(currentCourse)

            for dependentCourse in courseGraph[currentCourse]:
                courseIndegree[dependentCourse] -= 1
                if courseIndegree[dependentCourse] == 0:
                    readyCourses.append(dependentCourse)

        return len(completedCourses) == numCourses
