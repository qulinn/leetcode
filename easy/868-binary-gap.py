# Editorial: approach1: store indexes

class Solution:
    def binaryGap(self, n: int) -> int:
        # add index i to a when i-th bit == 1
        a = [i for i in range(32) if (n >> i) & 1]

        if len(a) < 2:
            return 0     
        return max(a[i+1]-a[i] for i in range(len(a)-1))


def test():
    solution = Solution()
    n = 22 # 22 in binary is "10110"
    print('output=',solution.binaryGap(n))
    

if __name__ == '__main__':
    test()

# for i in range(32):
#     print('n=', str(n), '>>',i,'->', n>>i, '& 1 ->', (n>>i)&1)
# for i in range(len(a)-1):
#     print('i=',i, ', a[i+1]=',a[i+1],'a[i]=',a[i], 'a[i+1]-a[i]=',a[i+1]-a[i])
# n= 22 >> 0 -> 22 & 1 -> 0
# n= 22 >> 1 -> 11 & 1 -> 1
# n= 22 >> 2 -> 5 & 1 -> 1
# n= 22 >> 3 -> 2 & 1 -> 0
# n= 22 >> 4 -> 1 & 1 -> 1
# n= 22 >> 5 -> 0 & 1 -> 0
# n= 22 >> 6 -> 0 & 1 -> 0
# n= 22 >> 7 -> 0 & 1 -> 0
# n= 22 >> 8 -> 0 & 1 -> 0
# n= 22 >> 9 -> 0 & 1 -> 0
# n= 22 >> 10 -> 0 & 1 -> 0
# n= 22 >> 11 -> 0 & 1 -> 0
# n= 22 >> 12 -> 0 & 1 -> 0
# n= 22 >> 13 -> 0 & 1 -> 0
# n= 22 >> 14 -> 0 & 1 -> 0
# n= 22 >> 15 -> 0 & 1 -> 0
# n= 22 >> 16 -> 0 & 1 -> 0
# n= 22 >> 17 -> 0 & 1 -> 0
# n= 22 >> 18 -> 0 & 1 -> 0
# n= 22 >> 19 -> 0 & 1 -> 0
# n= 22 >> 20 -> 0 & 1 -> 0
# n= 22 >> 21 -> 0 & 1 -> 0
# n= 22 >> 22 -> 0 & 1 -> 0
# n= 22 >> 23 -> 0 & 1 -> 0
# n= 22 >> 24 -> 0 & 1 -> 0
# n= 22 >> 25 -> 0 & 1 -> 0
# n= 22 >> 26 -> 0 & 1 -> 0
# n= 22 >> 27 -> 0 & 1 -> 0
# n= 22 >> 28 -> 0 & 1 -> 0
# n= 22 >> 29 -> 0 & 1 -> 0
# n= 22 >> 30 -> 0 & 1 -> 0
# n= 22 >> 31 -> 0 & 1 -> 0
# i= 0 , a[i+1]= 2 a[i]= 1 a[i+1]-a[i]= 1
# i= 1 , a[i+1]= 4 a[i]= 2 a[i+1]-a[i]= 2
# output= 2