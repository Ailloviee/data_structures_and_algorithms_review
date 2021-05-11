# Solution using a stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            elif c == "{":
                stack.append("}")
            else:
                if stack and stack.pop() == c:
                    continue
                else:
                    return False

        return len(stack) == 0
