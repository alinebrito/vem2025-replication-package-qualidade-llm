class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def dfs(course):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False

            visited[course] = -1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True