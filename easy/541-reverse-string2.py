class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 0:k ->reverse
        # k+1:2k -> doNothing
        #python3 doesn't have xrange()
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
