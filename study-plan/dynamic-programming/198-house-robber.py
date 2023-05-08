class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        rob_next_plus_one = 0
        rob_next = nums[n-1]

        for i in range(n-2, -1, -1):
            current = max(rob_next, rob_next_plus_one + nums[i])
            rob_next_plus_one = rob_next
            rob_next = current
        
        return rob_next

        # 1,2,3,1
        # n = 4
        # plusone = 0
        # next = 1
        
        # current = max(1, 0+3) = 3
        # plusone = 1
        # next = 3

        # current = max(3, 1+2) = 3
        # plusone = 3
        # rob_next = 3

        # current = max(3, 3+1) = 4
        # plusone = 3
        # next = 4 return 
        