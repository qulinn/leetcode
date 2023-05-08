import collections
class Solution:
    def intersection(self, nums):

        d = collections.defaultdict(int)
        ans = []
        for i in nums[0]:
            d[i] += 1

        for i in range(1, len(nums)):
            s = set(nums[i])
            for j in s:
                if j in d.keys():
                    d[j] += 1
        for i in d.keys():
            if d[i] == len(nums):
                ans.append(i)
        ans.sort()
        
        return ans

if __name__ == "__main__":
    nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
    test = Solution()
    expected_answer = [10, 12, 13, 27, 45]
    assert(test.intersection(nums) == expected_answer)