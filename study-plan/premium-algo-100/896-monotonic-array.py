class Solution:
    def isMonotonic(self, nums) -> bool:
        return (all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) 
            or all(nums[i] >= nums[i+1] for i in range(len(nums)-1)))

def test():
    input1 = [1,2,3]
    input2 = [3,2,1]
    input3 = [1,1,1]
    input4 = [1]
    input5 = [1,0,2,3]

    test = Solution()
    assert test.isMonotonic(input1) == True
    assert test.isMonotonic(input2) == True
    assert test.isMonotonic(input3) == True
    assert test.isMonotonic(input4) == True
    assert test.isMonotonic(input5) == False

if __name__ == '__main__':
    test()