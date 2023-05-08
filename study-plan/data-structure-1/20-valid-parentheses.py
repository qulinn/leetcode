import collections


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        container = collections.deque()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                container.append(i)
            elif container:
                if i == ")" and container.pop() != "(":
                    return False
                elif i == "}" and container.pop() != "{":
                    return False
                elif i == "]" and container.pop() != "[":
                    return False
            else:
                return False
        if not container:
            return True


if __name__ == "__main__":
    s = "()[]{}"
    test = Solution()
    assert(test.isValid(s) == True)
    print("Done")
