import collections


class Solution:
    def plusOne(self, digits: list) -> list:
        if len(digits) == 0:
            return 1
        nums = 1
        for i in range(len(digits)):
            nums += digits[i] * 10 **(len(digits) - i - 1)
        result = collections.deque()
        while True:
            a = nums // 10
            b = nums % 10
            result.appendleft(b)
            if a == 0:
                break
            nums = a
        return list(result)



if __name__ == '__main__':
    digits = [1,2,3]
    expected_output = [1,2,4]
    test = Solution()
    assert(test.plusOne(digits) == expected_output)
    print(":)")