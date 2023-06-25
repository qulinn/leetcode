class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #input a:str b:str
        #output sum:str
        #1<=a.length, b.length <=10^4
        # 11+1 = 100
        
        x,y = int(a,2), int(b,2) #2進数
        while y:
            answer = x^y
            carry = (x&y) << 1
            x,y = answer,carry
        return bin(x)[2:]
        #bin(): The bin() method converts a specified integer number to its binary representation and returns it.