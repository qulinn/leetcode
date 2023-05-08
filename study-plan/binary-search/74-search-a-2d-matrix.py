class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for i in range(len(matrix)):
            nums.extend(matrix[i])      
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return False