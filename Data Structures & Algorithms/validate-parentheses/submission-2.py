class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Dictionary setup
        d = {}
        d[']'] = '['
        d[')'] = '('
        d['}'] = '{'


        for char in s:
            if char in d:
                if len(stack) == 0 or stack[-1] != d[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


