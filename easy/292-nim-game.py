class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0 
        # in order to win, you have to ensure that you never reach 
        # the situation where there are exactly four stones on the 
        # pile on your turn.