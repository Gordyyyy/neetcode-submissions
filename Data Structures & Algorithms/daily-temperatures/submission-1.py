class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # I will be storing index in stack.
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                target = stack.pop()
                result[target] = i - target
            stack.append(i)
        return result
