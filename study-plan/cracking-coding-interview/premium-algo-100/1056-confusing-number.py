# cf. Implementation example in Editorial

class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        rotated_number = []

        for c in str(n):
            if c not in invert:
                return False
            rotated_number.append(invert[c])
        
        rotated_number = ''.join(rotated_number)
        return int(rotated_number[::-1]) != n
