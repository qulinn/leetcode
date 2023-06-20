class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = sorted(nums)
        if n[-1] >= n[-2]*2:
            for i,num in enumerate(nums):
                if num == n[-1]:
                    return i
        else:
            return -1
