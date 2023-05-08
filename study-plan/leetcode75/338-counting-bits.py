class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        b = 1
        
        # [0, b) is calculated
        while b <= n:
            # print('--')
            # print(x,b,n)
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                # print(x,x+b)
                ans[x + b] = ans[x] + 1
                # print(ans)
                x += 1
            x = 0 # reset x
            b <<= 1 # b = 2b
            
        return ans            