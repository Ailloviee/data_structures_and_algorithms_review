import math

# Solution using a stack to keep temporary results
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "*", "/"])

        for t in tokens:
            if not t in ops:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                elif t == "/":
                    stack.append(int(b / a))

        return stack[-1]
