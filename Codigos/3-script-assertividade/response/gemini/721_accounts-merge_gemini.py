class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        self.parents = list(range(n))

        def find(x):
            if self.parents[x] != x:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                self.parents[root_x] = root_y

        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])
                else:
                    email_to_index[email] = i

        merged_accounts = {}
        for i in range(n):
            parent = find(i)
            if parent not in merged_accounts:
                merged_accounts[parent] = set()
            merged_accounts[parent].update(accounts[i][1:])

        result = []
        for i, emails in merged_accounts.items():
            result.append([accounts[i][0]] + sorted(emails))
        return result