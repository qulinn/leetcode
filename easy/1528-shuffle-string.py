class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = [''] * len(s)

        for i,c in enumerate(s):
            output[indices[i]] = c
            
        return ''.join(output)
