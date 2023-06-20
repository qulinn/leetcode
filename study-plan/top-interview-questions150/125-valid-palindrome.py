class Solution:
    def isPalindrome(self, s: str) -> bool:
        #大文字と小文字を区別しない
        #大文字 to 小文字　-> str.lower()
        #小文字　to 大文字　-> str.upper()
        #記号は無視して良い
        #入力が空白の時はtrue
        #数字は入らない
        #str.isalnum() -> 英数字 -> True, 特殊文字 -> False
        
        string = ''.join(char for char in s if char.isalnum())
        
        for i in range(len(string)//2):
            if string[i].lower() != string[len(string)-i-1].lower():
                return False
        return True
    

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    test = Solution()
    assert(test.isPalindrome(s) == True)