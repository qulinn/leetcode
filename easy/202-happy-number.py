class Solution:
    def squareSum(self, n):
        result = 0
        while n > 0:
            left = n // 10
            digit = n % 10
            result += digit ** 2
            n = left
        return result
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.squareSum(n)
        while slow != fast and slow != 1 and fast != 1:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)        
        return slow == 1 or fast == 1

if __name__ == '__main__':
    num = 7
    test = Solution()
    assert(test.isHappy(num) == True)