class Solution:
    def toLowerCase(self, s: str) -> str:
        if len(s) == 0:
            return ""

        if s.islower():
            return s
        
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        d = dict(zip(upper, lower))

        return ''.join(d[x] if x in d else x for x in s)

def test():
    input1 = "Hello"
    input2 = "HeRe"
    input3 = "LOL"
    input4 = ""
    input5 = "abcde"
    output1 = "hello"
    output2 = "here"
    output3 = "lol"
    output4 = ""
    output5 = "abcde"

    test = Solution()
    assert test.toLowerCase(input1) == output1
    assert test.toLowerCase(input2) == output2
    assert test.toLowerCase(input3) == output3
    assert test.toLowerCase(input4) == output4
    assert test.toLowerCase(input5) == output5

if __name__ == '__main__':
    test()