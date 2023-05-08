class Solution:
    def removeDuplicates(self, nums:list) -> int:        
        #エッジケース
        if len(nums) == 0:
            return 0

        insert_index = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[insert_index]: 
                insert_index += 1
                nums[insert_index] = nums[j]
            
        return insert_index + 1

    #time: O(N)
    #space: O(C) = O(1)