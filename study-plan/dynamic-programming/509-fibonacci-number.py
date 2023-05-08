class Solution:
    def fib(self, n: int) -> int:
        # if n <=1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        
#         if n <= 1:
#             return n
#         cache = [0] * (n + 1)
#         cache[1] = 1
#         for i in range(2, n+1):
#             cache[i] = cache[i-1] + cache[i-2]
#         return cache[n]

        if n <= 1:
            return n
        current = 0
        prev1 = 1
        prev2 = 0
        for i in range(2,n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
        
