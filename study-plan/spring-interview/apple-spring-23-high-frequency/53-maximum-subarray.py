# Time: O(N) -> N is the length of the list
# Space: O(1)

class Solution:
    def maxSubArray(self, nums:list) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum



if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected_output = 6

    test = Solution()
    assert(test.maxSubArray(nums)==expected_output)
    print("Done")