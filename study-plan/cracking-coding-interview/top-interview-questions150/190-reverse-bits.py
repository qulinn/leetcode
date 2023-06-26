class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            #n&1で、最下位ビットと1のandをとって、retの先頭に置く
            ret += (n & 1) << power
            #次のループのための準備
            n = n >> 1
            power -= 1
        return ret