class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    expected_output = 4
    test = Solution()
    assert(test.numIdenticalPairs(nums) == expected_output)