class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d1 = collections.defaultdict(int)
        
        for w in words[0]:
            d1[w] += 1
        
        for i in range(1, len(words)):
            d2 = collections.defaultdict(int)
            for w in words[i]:
                d2[w] += 1
            for d in d1:
                d1[d] = min(d1[d], d2[d])
        
        output = []
        for d in d1:
            while d1[d] > 0:
                output.append(d)
                d1[d] -= 1
        return output
