class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate = []
        for i in nums:
            if i not in no_duplicate:
                no_duplicate.append(i)
            else:
                no_duplicate.remove(i)
        return no_duplicate.pop()