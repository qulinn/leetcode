class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #if: no two values have the same number of occurences -> true
        #else: false
        d = collections.defaultdict(int)
        for i in range(len(arr)):
            d[arr[i]]+= 1
        s = set()
        for i in d.keys():
            if d[i] in s:
                return False
            s.add(d[i])
        return True