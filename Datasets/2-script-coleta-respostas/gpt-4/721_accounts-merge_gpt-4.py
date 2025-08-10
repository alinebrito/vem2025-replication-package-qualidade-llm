class Solution:
    def accountsMerge(self, accounts):
        self.parents = {}
        self.emails = {}
        
        def find(email):
            if email != self.parents[email]:
                self.parents[email] = find(self.parents[email])
            return self.parents[email]
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.parents:
                    self.parents[email] = email
                self.emails[email] = name
                union_email = account[1]
                self.parents[find(email)] = find(union_email)
        
        merged = {}
        for email in self.parents:
            root = find(email)
            if root not in merged:
                merged[root] = set()
            merged[root].add(email)
        
        result = []
        for root, emails in merged.items():
            result.append([self.emails[root]] + sorted(emails))
        
        return result