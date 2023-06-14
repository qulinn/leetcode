class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        output = 0
        odd = False

        for c in count.values():
            output += int(c//2) * 2
            if output % 2 == 0 and c % 2 == 1:
                output += 1
            # if odd:
            #     if c > 1:
            #         if c % 2 == 0:
            #             output += c 
            #         else:
            #             #lowest even number of c
            #             output += c-1
            # else:
            #     if c % 2 == 0:
            #         output += c
            #     else:
            #         output += c
            #         odd = True

        return output
