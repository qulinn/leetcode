class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer


if __name__ == '__main__':
    n = 13
    expected_output = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13"]
    test = Solution()
    assert(test.fizzBuzz(n)==expected_output)