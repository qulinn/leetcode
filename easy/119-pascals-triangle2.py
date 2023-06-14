class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pas =[[1]]
        for i in range(1, rowIndex+1):
            temp = [1 for _ in range(i+1)]
            for j in range(1,len(temp)-1):
                temp[j] = pas[-1][j] + pas[-1][j-1]
            pas.append(temp)
        return pas[-1]

# [
#     [1]
#     [1,1]
#     [1,2,1]
#     [1,3,3,1]
# ]
