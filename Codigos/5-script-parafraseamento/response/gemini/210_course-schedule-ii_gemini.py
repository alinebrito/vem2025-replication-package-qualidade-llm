class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        stack = [i for i in range(numCourses) if indegree[i] == 0]
        order = []
        
        while stack:
            course = stack.pop()
            order.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    stack.append(next_course)
        
        return order if len(order) == numCourses else []