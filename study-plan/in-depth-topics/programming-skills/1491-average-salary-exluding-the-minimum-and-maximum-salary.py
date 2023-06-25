# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/solutions/3472407/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary)
        return (total - salary[0] - salary[-1]) / (len(salary) - 2)
