class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = triangle[row-1][col-1]
                    # print("col > 0", row, col, smallest_above)
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                    # print("col < row", row, col, smallest_above)
                triangle[row][col] += smallest_above
                # print(triangle[row][col])
        return min(triangle[-1])


        # if len(triangle) == 1:
        #     return triangle[0][0]

        # path = triangle[0][0]
        # i = 0
        # for j in range(1, len(triangle)):
        #     if triangle[j][i] < triangle[j][i+1]:
        #         path += triangle[j][i]
        #     else:
        #         path += triangle[j][i+1]
        #         i += 1
        
        # return path

