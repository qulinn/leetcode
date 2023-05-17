class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        max_sum = curr = sum(nums[:k])
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            if curr > max_sum:
                max_sum = curr
        return max_sum / k
    
if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    expected_output = 12.75000
    test = Solution()
    assert(test.findMaxAverage(nums,k) == expected_output)