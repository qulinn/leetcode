class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)

        if n <= 1:
            return 0

        cols_del = set()

        for i in range(n-1):
            for j, (c1,c2) in enumerate(zip(strs[i], strs[i+1])):
                if (j not in cols_del) and c1 > c2:
                    cols_del.add(j)
        
        return len(cols_del)
