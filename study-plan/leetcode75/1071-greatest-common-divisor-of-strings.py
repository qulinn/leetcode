class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        st = ""
        s = ""
        count = 0
        for i in range(min(len1,len2)):
            if str1[i] != str2[i]:
                break
            s += str1[i]
            count += 1
            if len1 % count == 0 and len2 % count == 0:
                if s*(len1//count) == str1 and s*(len2//count) == str2:
                    st = s
        return st