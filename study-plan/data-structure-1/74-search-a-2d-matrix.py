class Solution:
    def searchMatrix(self, matrix:list, target: int) -> bool:
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


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    test = Solution()
    assert(test.searchMatrix(matrix, target) == True)