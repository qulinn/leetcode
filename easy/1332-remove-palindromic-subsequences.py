class Solution:
    def isPalindrome(self, s:str):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def removePalindromeSub(self, s: str) -> int:
        # if not s:
        #     return 0
        # if s == s[::-1]:
        #     return 1
        # return 2
        
        if not s:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2
        

