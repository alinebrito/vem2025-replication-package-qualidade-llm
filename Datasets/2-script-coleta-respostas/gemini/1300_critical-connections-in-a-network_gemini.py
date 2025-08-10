class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for connection in connections:
            edgeMap[connection[0]].append(connection[1])
            edgeMap[connection[1]].append(connection[0])
        disc = [-1] * n
        low = [-1] * n
        time = 0
        res = []
        self.dfs(0, -1, edgeMap, disc, low, time, res)
        return res
    
    def dfs(self, currNode, prevNode, edgeMap, disc, low, time, res):
        disc[currNode] = time
        low[currNode] = time
        time += 1
        for nextNode in edgeMap[currNode]:
            if nextNode == prevNode:
                continue
            if disc[nextNode] == -1:
                self.dfs(nextNode, currNode, edgeMap, disc, low, time, res)
                low[currNode] = min(low[currNode], low[nextNode])
                if low[nextNode] > disc[currNode]:
                    res.append([currNode, nextNode])
            else:
                low[currNode] = min(low[currNode], disc[nextNode]) 