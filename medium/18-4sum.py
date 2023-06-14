class Solution:
    def twoSum(self, nums, target):
        res = []
        low, high = 0, len(nums) - 1
        while low < high:
            curr_sum = nums[low] + nums[high]
            if curr_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif curr_sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                high -= 1
            else:
                res.append([nums[low], nums[high]])
                low += 1
                high -= 1
        return res

    def kSum(self, nums, target, k):
        res = []
        
        if not nums:
            return res
        average_value = target // k

        if average_value < nums[0] or nums[-1] < average_value:
            return res
        
        if k == 2:
            return self.twoSum(nums,target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in self.kSum(nums[i+1:], target - nums[i], k-1):
                    res.append([nums[i]]+subset)
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)