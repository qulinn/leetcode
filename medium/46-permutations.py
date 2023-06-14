class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtrack(res, visited, [], nums)
        return res
        
    def backtrack(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(res, visited, subset+[nums[i]], nums)
                visited.remove(i)
