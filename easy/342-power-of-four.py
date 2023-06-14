class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        max_power = 15
        nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i-1]
        
        if n in nums:
            return True
        return False

