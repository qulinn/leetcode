class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            name,domain = email.split('@')
            local = name.split('+')[0].replace('.','')
            uniqueEmails.add(local + '@' + domain)
        return len(uniqueEmails)
