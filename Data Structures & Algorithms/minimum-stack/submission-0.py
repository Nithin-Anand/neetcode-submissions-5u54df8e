class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_element or self.min_element[-1] > val:
            self.min_element.append(val)
        else:
            self.min_element.append(self.min_element[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_element.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element[-1]
        
