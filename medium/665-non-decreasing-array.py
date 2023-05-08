class Solution:
    def checkPossibility(self, nums) -> bool:
        #if nums[i-2] > nums[i]:
        #nums[i] = nums[i-1]
        #else:
        #nums[i-1] = nums[i]
        
        #swap the two numbers in actual
        
        if len(nums) < 3:
            return True
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if count == 1:
                    return False
                count += 1
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True



if __name__ == '__main__':
    input = [3,4,2,3]
    expected_output = False
    test = Solution()
    assert(test.checkPossibility(input) == expected_output)
