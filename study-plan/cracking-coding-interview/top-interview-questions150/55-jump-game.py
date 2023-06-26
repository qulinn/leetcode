# https://leetcode.com/problems/jump-game/solutions/3653785/python-dp-memo-solution/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canJump(self, nums:list) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(1, nums[i]+1):
                    if i + j < n:
                        dp[i+j] = True
                    if i + j == n - 1:
                        return True
        return dp[n-1]



def test():
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    
    test = Solution()
    assert test.canJump(nums1) == True
    assert test.canJump(nums2) == False
    
    # nums1 = [2,3,1,1,4]
    # n=5
    # dp = [True, False, False, False, False]
    # i = 0
    # dp[0] == True -> j=[1,2]
    # j=1, i+j=1<n, dp[1]=True -> [True, True, False, False, False]
    # j=2, i+j=2<n, dp[2]=True -> [True, True, True, False, False]
    # i = 1
    # dp[1] == True -> j=[1,3]
    # j=1, i+j=2<n, dp[2]=True -> [True, True, True, False, False]
    # j=2, i+j=3<n, dp[3]=True -> [True, True, True, True, False]
    # j=3, i+j=4 == n-1, return True

    # nums2 = [3,2,1,0,4]
    # n=5
    # dp = [True, False, False, False, False]
    # i = 0
    # dp[0] == True -> j=[1,3]
    # j=1, i+j<n, [True, True, False, False, False]
    # j=2, i+j<n, [True, True, True, False, False]
    # j=3, i+j<n, [True, True, True, True, False]
    # i = 1
    # dp[1] == True -> j=[1,2]
    # j=1, i+j=2<n, [True, True, True, True, False]
    # j=2, i+j=3<n, [True, True, True, True, False]
    # i = 2
    # dp[2] == True -> j=1
    # j=1, i+j=3<n, [True, True, True, True, False]   
    # i = 3
    # dp[3] == True -> j=[1,0]
    # i = 4
    # dp[4] == False
    # return dp[n-1]=False



if __name__ == '__main__':
    test()