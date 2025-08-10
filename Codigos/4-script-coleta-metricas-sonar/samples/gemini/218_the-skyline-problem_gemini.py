class Solution:
from sortedcontainers import SortedList
class Solution:
  def getSkyline(self, buildings):
    events = []
    for l, r, h in buildings:
      events.append((l, h, 1))
      events.append((r, h, -1))
    events.sort()
    skyline = []
    heights = SortedList([0])
    prev = 0
    for x, h, t in events:
      if t == 1:
        heights.add(h)
      else:
        heights.remove(h)
      curr = heights[-1]
      if curr != prev:
        skyline.append([x, curr])
        prev = curr
    return skyline