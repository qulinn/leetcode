class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
                

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    expected_answer = 4
    test = Solution()
    assert(test.search(nums,target) == expected_answer)