class MinStack:
    # All function run in O(1)

    def __init__(self):
        self.stack = []
        self.smallestStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smallestStack:
            self.smallestStack.append(val)
        else:
            if val <= self.smallestStack[-1]:
                self.smallestStack.append(val)
        
    def pop(self) -> None:
        poppedItem = self.stack.pop()
        if poppedItem == self.smallestStack[-1]:
            self.smallestStack.pop()    

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.smallestStack[-1]

        
