class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        # print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            # print("i,c =",i, c)
            j = max(j, last[c])
            # print("j =",j)
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
                # print("ans: ", ans)
                # print("anchor: ", anchor)
        return ans



# {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
# i,c = 0 a
# j = 8
# i,c = 1 b
# j = 8
# i,c = 2 a
# j = 8
# i,c = 3 b
# j = 8
# i,c = 4 c
# j = 8
# i,c = 5 b
# j = 8
# i,c = 6 a
# j = 8
# i,c = 7 c
# j = 8
# i,c = 8 a
# j = 8
# ans:  [9]
# anchor:  9
# i,c = 9 d
# j = 14
# i,c = 10 e
# j = 15
# i,c = 11 f
# j = 15
# i,c = 12 e
# j = 15
# i,c = 13 g
# j = 15
# i,c = 14 d
# j = 15
# i,c = 15 e
# j = 15
# ans:  [9, 7]
# anchor:  16
# i,c = 16 h
# j = 19
# i,c = 17 i
# j = 22
# i,c = 18 j
# j = 23
# i,c = 19 h
# j = 23
# i,c = 20 k
# j = 23
# i,c = 21 l
# j = 23
# i,c = 22 i
# j = 23
# i,c = 23 j
# j = 23
# ans:  [9, 7, 8]
# anchor:  24

