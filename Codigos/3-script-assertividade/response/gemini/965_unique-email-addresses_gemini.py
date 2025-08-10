class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            return local + '@' + domain

        unique_emails = set()
        for email in emails:
            unique_emails.add(parse(email))
        return len(unique_emails)