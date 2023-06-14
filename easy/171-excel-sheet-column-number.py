class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        n = len(columnTitle)
        for i in range(n):
            ans = ans * 26
            ans += (ord(columnTitle[i]) - ord('A') + 1)
        return ans
