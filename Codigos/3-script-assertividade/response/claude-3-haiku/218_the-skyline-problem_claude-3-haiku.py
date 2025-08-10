class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        events = []
        for left, right, height in buildings:
            events.append((left, -height, 0))
            events.append((right, 0, 1))
        events.sort()
        
        heap = [0]
        max_height = 0
        for x, height, is_end in events:
            while x >= events[heap[0]][0]:
                heapq.heappop(heap)
            if is_end:
                heapq.heappush(heap, height)
            else:
                heapq.heappush(heap, height)
            current_height = -heap[0]
            if current_height != max_height:
                skyline.append([x, current_height])
                max_height = current_height
        return skyline