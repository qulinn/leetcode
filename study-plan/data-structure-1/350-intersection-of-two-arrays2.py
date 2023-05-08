import collections
class Solution:
    def intersect(self, nums1, nums2):
        d = collections.defaultdict(int)
        for i in nums1:
            d[i] += 1
        
        answer = []
        for i in nums2:
            if d[i] >= 1:
                answer.append(i)
                d[i] -= 1
        return answer



if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expected_output = [2,2]
    test = Solution()
    assert(test.intersect(nums1, nums2) == expected_output)