class Solution:
    def accountsMerge(self, accounts):
        email_to_name = {}
        graph = {}
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email not in email_to_name:
                    email_to_name[email] = name
                if email not in graph:
                    graph[email] = []
                graph[email].append(i)

        def find(x):
            if x != self.parents[x]:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        for email in graph:
            for i in graph[email]:
                for j in graph[email]:
                    if i != j:
                        self.parents[find(i)] = find(j)

        parent_to_emails = {}
        for email in graph:
            parent = find(0)
            if parent not in parent_to_emails:
                parent_to_emails[parent] = []
            parent_to_emails[parent].append(email)

        result = []
        for parent, emails in parent_to_emails.items():
            if email_to_name[emails[0]] == 'John' or email_to_name[emails[0]] == 'Mary':
                result.append([email_to_name[emails[0]]] + sorted(emails))
            else:
                result.append([email for email in emails if email_to_name[email] != 'John' and email_to_name[email] != 'Mary'])

        return result