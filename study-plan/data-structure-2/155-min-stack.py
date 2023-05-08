class MinStack:
    
    def __init__(self):
        self.stack = []
        self.list = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.list) == 0:
            self.list.append(val)
        else:
            if val < self.list[-1]:
                self.list.append(val)
            else:
                self.list.append(self.list[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.list.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.list[-1]
        


if __name__ == '__main__':
    minstack = MinStack()
    minstack.push(-2)
    minstack.push(0)
    minstack.push(-3)
    assert(minstack.getMin() == -3)
    minstack.pop()
    assert(minstack.top() == 0)
    assert(minstack.getMin() == -2)