class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = len(s)
        count = 0
        
        while i > 0:
            i -= 1
            if s[i] != " ":
                count += 1
            elif count > 0:
                return count
        return count