class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]



if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    expected_output = [5,6,7,1,2,3,4]
    test = Solution()
    test.rotate(nums,k)
    assert(nums == expected_output)