class Solution:
    def pivotIndex(self, nums:list) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for i,x in enumerate(nums):
            if left_sum == (right_sum - left_sum - x):
                return i
            left_sum += x
        return -1

if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    expected_output = 3
    test = Solution()
    assert(test.pivotIndex(nums)==expected_output)
