# editorial: approach 2: recored each move
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # n stands for the size of the boaord, n = 3 for the current game
        n = 3

        # use rows and cols to record the value on each row and each column
        # diag1 and diag2 to record value on diagnoal or anti-diagnoal
        rows, cols, = [0]*n, [0]*n
        diag = anti_diag = 0

        # two players having value of 1 and -1 
        # player1 playes first (value = 1)
        player = 1

        for row, col in moves:
            # update the row value and column value
            rows[row] += player
            cols[col] += player

            # if this move is placed on diagnoal or diagnoal,
            # we shall update the relative value as well.
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
            
            # check if this move meets any of the winning conditions
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return 'A' if player == 1 else 'B'
            
            # if no one wins so far, change to the other player alternatively.
            # that is from 1 to -1, from -1 to 1
            player *= -1

        # If all moves are completed and there's still no result, we shall check if 
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending"
