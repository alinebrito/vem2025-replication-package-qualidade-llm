class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        order = []
        while stack:
            course = stack.pop()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
        return order if len(order) == numCourses else []