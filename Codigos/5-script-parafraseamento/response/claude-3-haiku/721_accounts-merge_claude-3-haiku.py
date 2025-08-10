class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            parent[xroot] = yroot

        email_to_name = {}
        parent = {}

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                    email_to_name[email] = name
                union(parent, acc[1], email)

        ans = collections.defaultdict(list)
        for email in parent:
            ans[find(parent, email)].append(email)

        return [[""] + sorted(emails) for emails in ans.values()]