class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = []
        for line in accounts:
            sum = 0
            for i in line:
                sum += i
            output.append(sum)
        return max(output)