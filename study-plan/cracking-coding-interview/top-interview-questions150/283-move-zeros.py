class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[right] == 0:
                right += 1
            else:
                nums[left] = nums[right]
                nums[right] = 0
        return nums

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    expected_output = [1,3,12,0,0]
    test = Solution()
    assert(test.moveZeroes(nums) == expected_output)
