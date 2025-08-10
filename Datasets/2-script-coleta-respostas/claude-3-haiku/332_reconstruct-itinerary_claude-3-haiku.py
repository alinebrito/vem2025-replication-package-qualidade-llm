class Solution:
    def findItinerary(self, tickets):
        tickets.sort(reverse=True)
        graph = {}
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)
        
        route = []
        def dfs(src):
            while graph.get(src, []):
                dst = graph[src].pop()
                dfs(dst)
            route.append(src)
        
        dfs("JFK")
        return route[::-1]