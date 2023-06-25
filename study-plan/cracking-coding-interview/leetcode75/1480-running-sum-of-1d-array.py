class Solution:
    def runningSum(self, nums):
        result = []
        
        if len(nums) < 1:
            result.append(0)
            return result
        
        result.append(nums[0])
        for i in range(1,len(nums)):
            result.append(result[-1] + nums[i])
        
        return result


if __name__ == '__main__':
    nums = [1,2,3,4]
    expected_output = [1, 3, 6, 10]
    test = Solution()
    assert(test.runningSum(nums) == expected_output)