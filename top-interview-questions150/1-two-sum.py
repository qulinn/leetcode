class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        index = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
                
if __name__ == '__main__':
    test = Solution()
    nums = [2,7,11,15]
    target = 9
    expected_output = [0,1]
    assert(test.twoSum(nums, target)==expected_output)
    print("Done.")