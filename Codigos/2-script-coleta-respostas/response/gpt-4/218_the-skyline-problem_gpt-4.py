class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height))
            events.append((right, height))
        events.sort()

        result = []
        heights = SortedList([0])
        prev_height = 0

        for x, h in events:
            if h < 0:
                heights.add(-h)
            else:
                heights.remove(h)

            current_height = heights[-1]
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result