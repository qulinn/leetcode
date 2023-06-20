class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        prod2 = prod3 = prod5 = 0
        for i in range(1, n): #n=12
            a = ans[prod2]*2 
#a=[2,4,4,6,6,8,10,10,12]
            b = ans[prod3]*3
# b=[3,3,6,6,6,9,9,12,12]
            c = ans[prod5]*5
# c=[5,5,5,5,10,10,10,10,15]
            minN = min(a,b,c)
# print(a,b,c,minN)
# 2 3 5 2
# 4 3 5 3
# 4 6 5 4
# 6 6 5 5
# 6 6 10 6
# 8 9 10 8
# 10 9 10 9
# 10 12 10 10
# 12 12 15 12
            ans.append(minN)
            if minN == a:
                prod2 += 1
            if minN == b:
                prod3 += 1
            if minN == c:
                prod5 += 1
        return ans[-1]


def main():
    """
    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    """
    test = Solution()
    assert test.nthUglyNumber(n=10) == 12



if __name__ == '__main__':
    main()