class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            output.append(i*i)
        output.sort()
        return output
