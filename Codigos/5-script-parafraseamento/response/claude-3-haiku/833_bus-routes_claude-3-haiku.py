class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        n = len(routes)
        graph = collections.defaultdict(set)
        for i in range(n):
            for stop in routes[i]:
                graph[stop].add(i)
        
        queue = [(source, 0)]
        visited = set([source])
        while queue:
            stop, buses = queue.pop(0)
            if stop == target:
                return buses
            for bus in graph[stop]:
                for s in routes[bus]:
                    if s not in visited:
                        visited.add(s)
                        queue.append((s, buses + 1))
                routes[bus] = []
        
        return -1