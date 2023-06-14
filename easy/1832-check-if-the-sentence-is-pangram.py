class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp = "abcdefghijklmnopqrstuvwxyz"
        alp_set = set(list(alp))
        s = set(list(sentence))

        for i in s:
            if i in alp_set:
                alp_set.remove(i)
        
        if len(alp_set) == 0:
            return True
        return False
