class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        x,y,z = 0,1,1
        for _ in range(n-2):
            x,y,z = y, z, x+y+z
        return z
        
