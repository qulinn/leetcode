# https://leetcode.com/problems/powx-n/solutions/3620249/simple-solution-for-python/?envType=study-plan-v2&envId=programming-skills


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1.0 / x

        result = self.myPow(x, n//2)
        
        if n % 2 == 0:
            return result * result
        else:
            return x * result * result
