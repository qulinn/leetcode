class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for n in needle:
            if n not in haystack:
                return -1

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    test = Solution()
    expected_output = 2
    assert(test.strStr(haystack, needle)==expected_output)
    print(":)")