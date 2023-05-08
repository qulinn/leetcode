class Solution:
    def generate(self, numRows: int) -> list:
            triangle =[]

            for row_num in range(numRows):
                row = [None for _ in range(row_num+1)]
                row[0], row[-1] = 1, 1

                for j in range(1, len(row)-1):
                    row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
                triangle.append(row)
            return triangle


if __name__ == '__main__':
    numRows = 5
    expected_output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    test = Solution()
    assert(test.generate(numRows) == expected_output)
    print(":)")