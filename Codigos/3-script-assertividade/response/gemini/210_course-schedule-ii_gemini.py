class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        result = []

        for course, pre in prerequisites:
            graph[pre].append(course)

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
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result