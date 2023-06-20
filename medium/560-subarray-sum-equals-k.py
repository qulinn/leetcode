class Solution:
    def subarraySum(self, nums:list, k:int) -> int:
        count = 0
        sum = 0
        map = {0:1}

        for n in nums:
            sum += n
            diff = sum - k
            count += map.get(diff,0)
            map[sum] = 1 + map.get(sum, 0)

        return count

def main():
    """
        Input: nums = [1,1,1], k = 2
        Output: 2
    """
    test = Solution()
    assert test.subarraySum(nums=[1,1,1], k=2) == 2


if __name__ == '__main__':
    main()