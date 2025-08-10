class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for u, v in connections:
            edgeMap[u].append(v)
            edgeMap[v].append(u)

        disc = [-1]*n
        low = [0]*n
        self.time = 0
        res = []
        
        def dfs(node, parent):
            if disc[node] == -1:
                disc[node] = self.time
                low[node] = self.time
                self.time += 1
                
                for neighbor in edgeMap[node]:
                    if disc[neighbor] == -1:
                        dfs(neighbor, node)
                        
                    if neighbor != parent:
                        low[node] = min(low[node], low[neighbor])
                    
                    if low[neighbor]>disc[node]:
                        res.append([node, neighbor])

                        
                return True
            
            
        
        dfs(0,-1) 
        
        return res
