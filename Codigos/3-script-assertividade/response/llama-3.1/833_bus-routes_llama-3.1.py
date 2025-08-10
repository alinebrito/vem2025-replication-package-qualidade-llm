class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        bus_stops = set()
        bus_routes = {}
        for i, route in enumerate(routes):
            for stop in route:
                bus_stops.add(stop)
            bus_routes[i] = route

        visited = set()
        queue = [(source, 0)]
        while queue:
            stop, bus = queue.pop(0)
            if stop == target:
                return bus
            for i, route in bus_routes.items():
                if i not in visited:
                    visited.add(i)
                    for r in route:
                        if r in bus_stops:
                            queue.append((r, bus + 1))
        return -1