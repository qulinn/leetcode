# https://leetcode.com/problems/set-matrix-zeroes/solutions/3513736/python3-o-1-with-reverse-traversal/?envType=study-plan-v2&envId=programming-skills

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_val, R, C = 1, len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        first_row_val = 0
        
        for i in reversed(range(R)):
            for j in reversed(range(C)):
                if i == 0:
                    matrix[i][j] *= first_row_val
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    