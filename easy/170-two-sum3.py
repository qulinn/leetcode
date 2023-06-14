class TwoSum:

    def __init__(self):
        self.list = []
        

    def add(self, number: int) -> None:
        self.list.append(number)
        
        
    def find(self, value: int) -> bool:        
        seen = {}
        for i in range(len(self.list)):
            if value - self.list[i] in seen:
                return True
            seen[self.list[i]] = value - self.list[i]
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
