import numpy as np

class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        num = np.arange(1, n+1, 1)
        count = 0
        
        if len(num) < 1:
            return count
        else:
            for i in range(1, n+1):
                s = str(i)
                if '3' in s or '4' in s or '7' in s:
                    continue       
                elif '2' in s or '5' in s or '6' in s or '9' in s:
                    count = count + 1
                else: #'0' in s or '1' in s or '8' in s:
                    continue
                
            return count
