# https://leetcode.com/problems/buddy-strings/solutions/891275/python-best-simple-and-clean-explained-solution-o-n-o-1/?envType=study-plan-v2&envId=programming-skills



class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # check same length
        if len(s) != len(goal):
            return False

        # if strings are equal -> check if there is a double to swap
        if s == goal:
            return True if len(s) - len(set(s)) >= 1 else False

        # count differences between strings
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
            if len(diff) > 2:
                return False
        
        # not exactly two differences
        if len(diff) != 2:
            return False
        
        # check if can be swaqpped
        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
    
        return False
