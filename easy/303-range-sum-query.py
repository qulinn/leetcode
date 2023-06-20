class NumArray:

    def __init__(self, nums: List[int]):
        self.numarray = nums

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right+ 1):
            ans += self.numarray[i]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
