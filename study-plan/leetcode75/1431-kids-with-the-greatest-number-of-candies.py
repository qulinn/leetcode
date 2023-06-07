class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        max_candies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
    
if __name__ == '__main__':
    # Input: 
    candies = [2,3,5,1,3]
    extraCandies = 3
    # Output: 
    expected_output = [True,True,True,False,True] 
    test = Solution()
    assert test.kidsWithCandies(candies, extraCandies) == expected_output