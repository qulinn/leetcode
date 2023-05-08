class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

if __name__ == '__main__':
    num1 = 12
    num2 = 5
    total = num1 + num2
    test = Solution()
    assert(test.sum(num1, num2) == total)