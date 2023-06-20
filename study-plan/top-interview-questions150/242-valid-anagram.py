import collections



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = collections.defaultdict(int)
        dict_t = collections.defaultdict(int)
        for i in s:
            dict_s[i] += 1
        for i in t:
            dict_t[i] += 1
        
        if len(dict_s) != len(dict_t):
            return False
        
        for i in dict_s:
            if i not in dict_t:
                return False
            if dict_s[i] != dict_t[i]:
                return False
        return True
        


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    test = Solution()
    assert(test.isAnagram(s,t) == True)