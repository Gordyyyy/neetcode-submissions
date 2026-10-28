class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tempNum = 0
        stack = []
        operator = set()
        operator.add('*')
        operator.add('+')
        operator.add('-')
        operator.add('/')

        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                tempNum = stack.pop() + stack.pop()
                stack.append(tempNum)
            elif tokens[i] == '-':
                tempNum = -(stack.pop() - stack.pop())
                stack.append(tempNum)
            elif tokens[i] == '*':
                tempNum = stack.pop() * stack.pop()
                stack.append(tempNum)
            elif tokens[i] == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                tempNum = int(num2 / num1)
                stack.append(tempNum)
        return stack[0]
