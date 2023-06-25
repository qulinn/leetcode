class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0 = set()
        ans1 = set()

        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                ans0.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                ans1.add(nums2[i])
        
        return [list(ans0), list(ans1)]