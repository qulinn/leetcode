class Solution:
    def climbStairs(self, n: int) -> int:
        #フィボナッチ数列
        if n == 1:
            return 1
        num = [_ for _ in range(n+1)]
        num[1] = 1
        num[2] = 2
        for i in range(3, n+1):
            num[i] = num[i-1] + num[i-2]
        return num[n]