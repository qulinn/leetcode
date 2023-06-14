class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        output = []

        for i in range(len(nums)):
            if i + 1 >= len(nums) or nums[i+1] - nums[i] != 1:
                begin = str(nums[start])
                end = str(nums[i])
                if begin != end:
                    output.append(begin + "->" + end)
                else:
                    output.append(begin)
                start = i + 1
        return output
