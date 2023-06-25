class Solution:
    def formatRange(self,lower,upper):
        if lower == upper:
            return str(lower)
        return str(lower)+"->"+str(upper)
    
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1
        for i in range(len(nums)+1):
            if i<len(nums):
                curr = nums[i]
            else:
                curr = upper+1
            if prev+1 <= curr-1:
                result.append(self.formatRange(prev+1,curr-1))
            prev = curr
        return result