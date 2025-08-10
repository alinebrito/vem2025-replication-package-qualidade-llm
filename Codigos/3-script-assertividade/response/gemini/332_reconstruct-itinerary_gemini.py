class Solution:
    def findItinerary(self, tickets):
        graph = {}
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = []
            graph[ticket[0]].append(ticket[1])

        for key in graph:
            graph[key].sort(reverse=True)

        itinerary = []
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                itinerary.append(stack.pop())
        return itinerary[::-1]