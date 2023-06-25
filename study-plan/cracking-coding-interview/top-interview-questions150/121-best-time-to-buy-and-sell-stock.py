def maxProfit(prices) -> int:
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

def maxProfit_(prices) -> int:
    min_price = float('int')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

def main():
    prices = [7,1,5,3,6,4]
    assert(maxProfit(prices) == 5)

if __name__ == '__main__':
    main()