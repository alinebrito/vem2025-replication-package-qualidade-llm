class Solution:
    def findItinerary(self, tickets):
        tickets.sort(reverse=True)
        flights = {}
        for a, b in tickets:
            if a not in flights:
                flights[a] = []
            flights[a].append(b)

        route = []
        def dfs(a):
            while a in flights and flights[a]:
                dfs(flights[a].pop())
            route.append(a)
        dfs('JFK')
        return route[::-1]