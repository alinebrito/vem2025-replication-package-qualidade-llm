class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            return local + '@' + domain
        
        return len(set(parse(email) for email in emails))