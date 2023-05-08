class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            flag = True
        else:
            flag = False

        result = 0
        while True:
            a = x // 10
            b = x % 10
            result += b * 10 **(len(str(x))-1)
            x = a
            if a == 0:
                break
        
        if flag == True:
            if -result <= -2**31:
                return 0
            return -result
        else:
            if result >= 2**31:
                return 0
            return result


if __name__ == '__main__':
    x = 123
    expected_output = 321
    test = Solution()
    assert(test.reverse(x)==expected_output)
    print("Done.")