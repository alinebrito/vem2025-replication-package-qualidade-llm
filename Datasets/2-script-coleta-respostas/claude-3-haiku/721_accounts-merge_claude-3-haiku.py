class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                self.parents[px] = py
        
        self.parents = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.parents:
                    self.parents[email] = email
                union(account[1], email)
        
        merged = collections.defaultdict(list)
        
        for email in self.parents:
            merged[find(email)].append(email)
        
        return [[name] + sorted(emails) for name, emails in merged.items()]