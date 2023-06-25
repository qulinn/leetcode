class Solution:
    def singleNumber(self, nums) -> int:
        no_duplicate = []
        for i in nums:
            if i not in no_duplicate:
                no_duplicate.append(i)
            else:
                no_duplicate.remove(i)
        return no_duplicate.pop()

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    expected_output = 4

    test = Solution()
    assert(test.singleNumber(nums) == expected_output)