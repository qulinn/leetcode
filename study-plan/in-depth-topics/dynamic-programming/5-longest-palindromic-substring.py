class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            ans = s[i]

        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(ans) <= len(s[i:j+1]):
                            ans = s[i:j+1]
        return ans

# print(i,j,s[i],s[j])
# 3 4 a d
# 2 3 b a
# 2 4 b d
# 1 2 a b
# 1 3 a a
# -> s[i]==s[j] -> dp[i+1][j-1]==dp[2][2]==True 
# -> dp[i][j]==dp[1][3]==True -> ans=s[1:4]="aba"
# 1 4 a d
# 0 1 b a
# 0 2 b b 
# -> s[i]==s[j] -> dp[i+1][j-1]==dp[1][1]==True
# ->dp[i][j]==dp[0][2]==True -> s[0:3]="bab" -> ans="bab"
# 0 3 b a
# 0 4 b d