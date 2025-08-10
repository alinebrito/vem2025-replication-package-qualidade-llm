class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        heap = []
        for _ in range(k):
            while projects and projects[0][0] <= w:
                _, profit = projects.pop(0)
                heapq.heappush(heap, -profit)
            if heap:
                w -= heapq.heappop(heap)
        return w