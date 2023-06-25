class Solution:
    def containsDuplicate(self, nums) -> bool:
        counter=set()
        
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    test = Solution()
    assert(test.containsDuplicate(nums) == True)