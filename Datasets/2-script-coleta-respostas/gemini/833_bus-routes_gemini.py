class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        n = len(routes)
        graph = [[] for _ in range(n)]
        stopToBus = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stopToBus:
                    stopToBus[stop] = []
                stopToBus[stop].append(i)
        for i in range(n):
            for j in range(i + 1, n):
                for stop1 in routes[i]:
                    for stop2 in routes[j]:
                        if stop1 == stop2:
                            graph[i].append(j)
                            graph[j].append(i)
                            break
        queue = [i for i in stopToBus[source]]
        visited = set(queue)
        buses = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        if target in routes[neighbor]:
                            return buses + 1
                        queue.append(neighbor)
                        visited.add(neighbor)
            buses += 1
        return -1