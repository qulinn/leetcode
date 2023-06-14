class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # n = len(nums)
        # m = len(queries)
        # return answer

        #nums = [4,5,2,1]
        #queries = [3,10,21]
        #nums[2]+nums[3] == queries[0], maximam size of the subsequence is 2
        #nums[0]+nums[1]+nums[3] < queries[1], maximum size of the subsequence is 3
        
        ans = []
        
        #sort nums
        nums.sort()
        
        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break
            ans.append(count)
        return ans
                
        
