class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
            
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        count = 0  
        while queue:
            course = queue.pop(0)
            count += 1  
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1  
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses  