class Solution:
    def __init__(self):
        pass
    def removeStones(self, stones):
        rows = {}
        cols = {}
        for i, (x, y) in enumerate(stones):
            if x not in rows:
                rows[x] = i
            if y not in cols:
                cols[y] = i

        removed = [False] * len(stones)
        count = 0
        for i, (x, y) in enumerate(stones):
            if removed[i]:
                continue
            
            can_remove = False
            for j, (x2, y2) in enumerate(stones):
                if i != j and not removed[j] and (x == x2 or y == y2):
                    can_remove = True
                    break

            if can_remove:
                removed[i] = True
                count += 1

        return count
