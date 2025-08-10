class Solution:
    def accountsMerge(self, accounts):
        self.parents = {}
        
        def find(email):
            if email != self.parents[email]:
                self.parents[email] = find(self.parents[email])
            return self.parents[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                self.parents[root1] = root2
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.parents:
                    self.parents[email] = email
                union(account[1], email)
        
        email_to_name = {}
        for email in self.parents:
            root = find(email)
            if root not in email_to_name:
                email_to_name[root] = []
            email_to_name[root].append(email)
        
        merged_accounts = []
        for root, emails in email_to_name.items():
            merged_accounts.append([accounts[0][0]] + sorted(emails))
        
        return merged_accounts