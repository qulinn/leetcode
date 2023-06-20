class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        ans = 1
        i = 2
        while i*i < num: 
            if num % i == 0: 
                ans += i + num // i
            i += 1 
        
        if i * i == num:
            ans += i
        
        return ans == num

    # i=2    # 2*2<28
    # 28%2==0 -> ans = 1+2+ 28//2 = 17
    # i=3 -> 3*3 < 28 -> 28%3!=0
    # i=4 -> 4*4 < 28 -> 28%4 = 0 -> ans = 17 + 4 + 28//4 = 28
    # i=5, i=6 ->ng
    # ans == num -> return True
