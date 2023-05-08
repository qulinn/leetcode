class Solution:
    def missingNumber(self, nums: list) -> int:
        #len(nums) = 3
        #-> 1+2+3 = 6
        #6-4=2
        #len(nums)>=1
        #numsの中身は全て異なる数字
        #O(N), N=len(nums)
        sum_n = sum([i for i in range(1, len(nums)+1)])
        #O(N), N=len(nums)
        sum_nums = sum(nums)
        
        return sum_n - sum_nums
        
if __name__ == '__main__':
    nums = [3,0,1]
    test = Solution()
    expected_output = 2
    assert(test.missingNumber(nums) == expected_output)