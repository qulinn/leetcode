class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0 
        ans = 0
        while right < len(nums) - 1: # 4 == 4
            max_jump = 0
            for i in range(left, right+1): # 1-3
                max_jump = max(max_jump, i + nums[i]) # 2 vs 1+3=4 -> 4
            left += 1 #2
            right = max_jump #4
            ans += 1 #2
        return ans
