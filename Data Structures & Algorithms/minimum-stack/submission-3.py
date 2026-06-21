class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)

        else:
            diff = val - self.min
            self.stack.append(diff)
            if diff < 0:
                self.min = val
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            raise IndexError            
        
        if self.stack[-1] < 0:
            self.min = self.min - self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return IndexError
        if self.stack[-1] < 0:
            return self.min
        else:
            return self.min + self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
