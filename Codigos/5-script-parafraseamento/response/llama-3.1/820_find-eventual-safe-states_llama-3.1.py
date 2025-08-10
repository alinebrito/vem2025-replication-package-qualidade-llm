class Solution:
    def dfs(self, adj, src, vis, recst):
        vis[src] = True
        recst[src] = True
        for neighbor in adj[src]:
            if not vis[neighbor]:
                if self.dfs(adj, neighbor, vis, recst):
                    return True
            elif recst[neighbor]:
                return True
        recst[src] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [False]*n
        recst = [False]*n
        safe = [True]*n
        
        for i in range(n):
            if self.dfs(graph, i ,vis ,recst):
                safe[i] = False
                
        
                
        
                
        
                
        
                
        
                
        
                
        
        
        
       return [i for i in range(n) if safe[i]]