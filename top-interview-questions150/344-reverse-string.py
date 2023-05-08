class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
            
        #left = 0
        #right = len(s)-1
        #while left < right:
        #    temp = s[left]
        #    s[left] = s[right]
        #    s[right] = temp
        #    left += 1
        #    right -= 1
        
        return s
if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    expected_output = ["o","l","l","e","h"]
    test = Solution()
    assert(test.reverseString(s) == expected_output)