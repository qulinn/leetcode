class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        leftsum = 0
        rightsum = sum(nums)

        for n in nums:
            leftsum += n
            ans.append(abs(leftsum-rightsum))
            rightsum -=n
        return ans