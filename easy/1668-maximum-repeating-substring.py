class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word) > len(sequence):
            return 0
        if len(word) == len(sequence) and word != sequence:
            return 0
        if word not in sequence:
            return 0

        temp = word
        ans = 0
        while temp in sequence:
            temp = temp + word
            ans += 1
        return ans
    