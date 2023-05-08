class Solution:
    def isValidSudoku(self, board) -> bool:
        N = 9

        row = [set() for _ in range(N)]
        column = [set() for _ in range(N)]
        block = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue   
                if board[r][c] in row[r]:
                    return False
                row[r].add(board[r][c])
                
                if board[r][c] in column[c]:
                    return False
                column[c].add(board[r][c])

                b = (r // 3)*3 +  c // 3
                if board[r][c] in block[b]:
                    return False
                block[b].add(board[r][c])
        return True



if __name__ == '__main__':
    sudoku = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    test = Solution()
    assert(test.isValidSudoku(sudoku)==True)
    print(":)")
