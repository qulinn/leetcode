import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransom = collections.defaultdict(int)
        d_magazine = collections.defaultdict(int)
        for i in ransomNote:
            d_ransom[i] += 1
        for i in magazine:
            d_magazine[i] += 1
        
        if len(d_ransom) > len(d_magazine):
            return False
        for i in d_ransom:
            if i not in d_magazine:
                return False
        for i in d_magazine:            
            if d_magazine[i] < d_ransom[i]:
                return False
        return True
            
if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    test = Solution()
    assert(test.canConstruct(ransomNote,magazine) == True)