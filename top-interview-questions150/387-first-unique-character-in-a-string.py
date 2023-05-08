import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        d = dict(d)
        for index, char in enumerate(s):
            if d[char] == 1:
                return index
        return -1
        

if __name__ == '__main__':
    string = "leetcode"
    test = Solution()
    assert(test.firstUniqChar(string) == 0)