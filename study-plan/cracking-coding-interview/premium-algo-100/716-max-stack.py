# cf. Editorial, approach1

from sortedcontainers import SortedList


class MaxStack:
    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.count = 0

    # push(x): push x onto the stack
    def push(self, x: int) -> None:
        self.stack.add((self.count, x))
        self.values.add((x, self.count))
        self.count += 1

    # pop():
    # remove the element on the top of the stack and return it
    def pop(self) -> int:
        index, val = self.stack.pop()
        self.values.remove((val, index))
        return val

    # top():
    # gets the element on the top of the stack without removing it
    def top(self) -> int:
        return self.stack[-1][1]

    # peekMax():
    # retrive the maximum element in the stack without removing it
    def peekMax(self) -> int:
        return self.values[-1][0]

    # popMax():
    # retrive the maximum element in the sack and remove it.
    # if there is moer than one maximum element, only remove
    # the top-most one.
    def popMax(self) -> int:
        val, index = self.values.pop()
        self.stack.remove((index, val))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
"""
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.
"""
