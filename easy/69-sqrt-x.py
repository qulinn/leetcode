class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search
        if x < 2:
            return x
        
        left = 2
        right = x//2
        while left <= right:
            mid = (left + right) // 2
            if mid*mid > x:
                right = mid - 1
            elif mid*mid < x:
                left = mid + 1
            else:
                return mid
        return right


if __name__ == '__main__':
    input = 8
    expected_output = 2
    test = Solution()
    assert(test.mySqrt(input) == expected_output)
    print(":)")