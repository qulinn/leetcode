class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        seen = set()
        output = set()

        for start in range(n-L+1):
            tmp = s[start:start+L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
        
