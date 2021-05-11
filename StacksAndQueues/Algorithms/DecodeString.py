# Solution using a stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_s = ""
        curr_k = 0

        for c in s:
            if c.isdigit():
                curr_k = 10 * curr_k + int(c)
            elif c == "[":
                stack.append(curr_k)
                stack.append(curr_s)
                curr_k = 0
                curr_s = ""
            elif c == "]":
                prev_s = stack.pop()
                curr_k = stack.pop()
                for _ in range(curr_k):
                    prev_s += curr_s
                curr_k = 0
                curr_s = prev_s
            else:
                curr_s += c

        return curr_s
