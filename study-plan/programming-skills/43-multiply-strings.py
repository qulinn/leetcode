class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        n = len(num1) + len(num2)
        ans = [0] * n
        
        #reverse num1 and num2
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        for place2, digit2 in enumerate(num2_rev):
            for place1, digit1 in enumerate(num1_rev):
                num_zeros = place1 + place2
                carry = ans[num_zeros]
                mul = int(digit1) * int(digit2) + carry
                ans[num_zeros] = mul % 10
                ans[num_zeros + 1] += mul // 10

        if ans[-1] == 0:
            ans.pop()
        return ''.join(str(digit) for digit in reversed(ans))