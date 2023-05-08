import collections
import enum


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)
        for i in s:
            dict_s[i] += 1
        for i in t:
            dict_t[i] += 1
        
        if len(dict_s) != len(dict_t):
            return False


        return True


if __name__ == "__main__":
    test = Solution()
    s = "egg"
    t = "add"
    test.isIsomorphic(s, t)
