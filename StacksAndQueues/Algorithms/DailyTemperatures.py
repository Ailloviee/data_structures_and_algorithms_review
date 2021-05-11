# Solution using a stack, traversing backwards, pop temperatures in the stack that are lower than the current temp and keep the higher ones
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []

        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            if not stack:
                stack.append(i)
            else:
                res[i] = stack[-1] - i
                stack.append(i)
        return res
