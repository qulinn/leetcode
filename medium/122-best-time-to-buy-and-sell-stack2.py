class Solution:
    
    def maxProfit(self, prices) -> int:
        #エッジケース
        if len(prices) == 0:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]    
    expected_output = 7

    test = Solution()
    assert(test.maxProfit(prices) == expected_output)
    print(":)")