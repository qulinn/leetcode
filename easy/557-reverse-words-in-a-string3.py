class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        reverse = []
        for i in l:
            r = i[::-1]
            reverse.append(r)
        res = ' '.join(i for i in reverse)
        return res
