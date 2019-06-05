"""
Min Max Stack Construction - Medium

Effecitvely implement a stack with min max properties
what is a stack?
Fundamental data structure, real life example: pile of books on a table
you can implement a linked list to do this however an array will do this


Time: O(1)
Space: O(1)
"""


class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


stack = MinMaxStack()
stack.push(4)
print(stack.peek())



print(stack)


































