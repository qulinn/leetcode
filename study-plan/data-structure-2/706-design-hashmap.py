class MyHashMap:

    def __init__(self):
        self.dict = {}
        
    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        if key in self.dict:
            return self.dict[key]
        return -1
    
    def remove(self, key: int) -> None:
        if key in self.dict:
            self.dict.pop(key)


if __name__ == '__main__':
    myhashmap = MyHashMap()
    myhashmap.put(1,1)
    myhashmap.put(2,2)
    assert(myhashmap.get(1) == 1)
    assert(myhashmap.get(3) == -1)
    myhashmap.put(2,1)
    assert(myhashmap.get(2) == 1)
    myhashmap.remove(2)
    assert(myhashmap.get(2))