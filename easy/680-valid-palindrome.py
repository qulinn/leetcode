class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.check_palindrome(s, left, right-1) or self.check_palindrome(s, left+1, right)
            left += 1
            right -= 1
        return True
        
    def check_palindrome(self, s, left, right) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    test = Solution()
    assert(test.validPalindrome("abc") == False)
    assert(test.validPalindrome("abba") == True)
    assert(test.validPalindrome("abbaa")== True)
    assert(test.validPalindrome("abca") == True)