class Solution:
    def find_itinerary(self, tickets):
        graph = {}
        for start, end in tickets:
            if start not in graph:
                graph[start] = []
            graph[start].append(end)
        for start in graph:
            graph[start].sort(reverse=True)

        itinerary = []
        
        def dfs(airport):
            while airport in graph and graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]