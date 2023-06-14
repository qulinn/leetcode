class Solution:
    def removeDuplicates(self, s: str) -> str:
        #abbaca
        #stack.push(s[0])
        # char = stack.pop()
        # if s[1] == char:
        #   check s[2]
        #else: stack.push(char)
        #return str(stack)

        # stack = collections.deque()
        # stack.append(s[0]) #a
        # for i in range(1, len(s)-1):
        #     if not stack:
        #         char = stack.pop() #a
        #         if s[i] != char: # c != a
        #             stack.append(char) #a
        #             stack.append(s[i]) #ac
        #         else: #b == b -> stack = a
        #             continue
        # return ''.join(stack)

        output = []
        for i in s:
            if output and i == output[-1]:
                output.pop()
            else:
                output.append(i)
        return ''.join(output)
