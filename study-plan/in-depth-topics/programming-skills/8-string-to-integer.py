class Solution:
    def myAtoi(self, s: str) -> int:
        #input -> output
        #'1234' -> 1234
        #'   4' -> 4
        #'12 4' -> 12
        flag = True
        result = 0
        index = 0
        n = len(s)

        int_max = 2**31 -1
        int_min = -2**31
        
        #先頭の空白を処理する
        while index < n and s[index] == ' ':
            index += 1
        
        #返り値の符号を決める
        if index < n and s[index] == '+':
            flag = True
            index += 1
        elif index < n and s[index] == '-':
            flag = False
            index += 1
        
        #check overflow とresult の計算
        while index < n and s[index].isdigit():
            digit = int(s[index])            
            result = result * 10 + digit
            index += 1
            if result > int_max or (result == int_max and digit > int_max % 10):
                return int_max if flag == True else int_min
        
        if flag == True:
            return result
        else:
            return -result