class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = {}
        for (a,b), v in zip(equations, values):
            if a not in G:
                G[a] = {}
            if b not in G:
                G[b] = {}
            G[a][b] = v
            G[b][a] = 1/v
            
        res = []
        for a,b in queries:
            if a not in G or b not in G:
                res.append(-1)
                continue
            stack = [(a,[a])]
            while stack:
                node,path=stack.pop()
                for nei,v in G[node].items():
                    if nei==b:
                        res.append(v)
                        break
                    elif nei not in path:
                        stack.append((nei,path+[nei]))
                else:
                    continue
                break
            else:
                res.append(-1)
                
        return res