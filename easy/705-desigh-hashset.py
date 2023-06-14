class MyHashSet:
#https://leetcode.com/problems/design-hashset/discuss/1969766/Python-Solution-Using-set()-Explained-oror-Faster-than-99.34
    def __init__(self):
        self.hashset = set([])

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False



