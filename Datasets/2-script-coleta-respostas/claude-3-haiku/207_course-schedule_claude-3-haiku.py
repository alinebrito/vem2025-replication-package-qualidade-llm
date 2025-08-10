class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = [course for course in range(numCourses) if indegree[course] == 0]
        count = 0
        
        while queue:
            course = queue.pop(0)
            count += 1
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses