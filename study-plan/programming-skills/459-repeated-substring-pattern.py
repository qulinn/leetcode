# https://leetcode.com/problems/repeated-substring-pattern/solutions/3278680/459-solution-with-step-by-step-explanation/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if s[:i] * (n // i) == s:
                    return True
        return False
    
"""
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Input: s = "aba"
Output: false
"""

def test():
    test = Solution()
    assert test.repeatedSubstringPattern("abcabcabcabc") == True
    assert test.repeatedSubstringPattern("aba") == False    

if __name__ == '__main__':
    test()