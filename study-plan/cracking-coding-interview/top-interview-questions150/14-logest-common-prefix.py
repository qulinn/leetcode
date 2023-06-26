class Solution:
    def longestCommonPrefix(self, strs):
        common = strs[0]
        for i in range(1, len(strs)):
            new_common = ''
            j = 0
            while j < len(common) and j < len(strs[i]):
                if common[j] == strs[i][j]:
                    new_common += common[j]
                    j += 1
                else:
                    break
            common = new_common
            if common == '':
                break
        return common

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    expected_output = "fl"
    test = Solution()
    assert(test.longestCommonPrefix(strs)==expected_output)
    print("Done")