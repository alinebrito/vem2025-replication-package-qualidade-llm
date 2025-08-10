class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        queue = [course for course in range(numCourses) if in_degree[course] == 0]
        result = []
        while queue:
            course = queue.pop(0)
            result.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []