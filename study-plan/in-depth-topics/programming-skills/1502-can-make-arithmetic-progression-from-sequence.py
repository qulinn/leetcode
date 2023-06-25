class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        if len(arr) < 2:
            return False

        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
def main():
    input1 = [3,5,1]
    input2 = [1,2,4]
    test = Solution()
    assert test.canMakeArithmeticProgression(input1) == True
    assert test.canMakeArithmeticProgression(input2) == False

if __name__ == '__main__':
    main()