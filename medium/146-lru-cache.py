class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.cache = {}


    def get(self, key: int) -> int:
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            self.cache[key] = value
            return None
        if len(self.cache) >= self.capacity:
            k = self.keys.pop(0)
            self.cache.pop(k)
            self.keys.append(key)
            self.cache[key] = value
            return None
        
        self.keys.append(key)
        self.cache[key] = value
        return None
                        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
