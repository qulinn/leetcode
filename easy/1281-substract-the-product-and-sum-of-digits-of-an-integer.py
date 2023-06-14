class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0

        while n > 0:
            b = n % 10
            product *= b
            total += b
            n = n //10
        
        return product - total
