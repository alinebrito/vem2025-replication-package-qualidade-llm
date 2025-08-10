class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        from collections import defaultdict, deque
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        queue = deque([(source, 0)])
        visited_stops = set([source])
        visited_routes = set()
        while queue:
            stop, buses = queue.popleft()
            for route in graph[stop]:
                if route in visited_routes:
                    continue
                visited_routes.add(route)
                for next_stop in routes[route]:
                    if next_stop == target:
                        return buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        return -1