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
        

#stackとlistを使って実装する
#stackは、通常のpush, pop の機能で実装する
#listは、値を1つpushした段階での、stack内の最小値を格納
#getMin()は、list[-1]を返す
#topてなに？　→　popしないでstackの一番上を参照
#stack = []で実装してstack[-1]を返せばいい

#
#
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()