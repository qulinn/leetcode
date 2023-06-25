class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #https://leetcode.com/problems/palindrome-permutation/discuss/1006994/Python-3-Hashmap(Dict)-Sets-TC:-O(n)-SC:-O(1)
        sets = set()
        for i in s:
            if i not in sets:
                sets.add(i)
            else:
                sets.remove(i)
        return (len(sets) <= 1)