class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        n = len(routes)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in routes[i]:
                for k in range(n):
                    if i != k and j in routes[k]:
                        graph[i].append(k)
        queue = [(source, 0)]
        seen = set([source])
        for stop, buses in queue:
            if stop == target:
                return buses
            for i in range(n):
                if stop in routes[i] and i not in seen:
                    seen.add(i)
                    queue.append((i, buses + 1))
        return -1