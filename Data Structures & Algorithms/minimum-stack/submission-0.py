class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixsmall = []
        self.i = 0

    def push(self, val: int) -> None:
        if self.i == 0:
            self.prefixsmall.append(val)
        else:
            self.prefixsmall.append(min(self.prefixsmall[-1], val))
        
        self.i += 1
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.i == 0:
            raise IndexError            
        
        self.stack = self.stack[0: -1]
        self.prefixsmall = self.prefixsmall[0: -1]

        self.i -= 1

    def top(self) -> int:
        if self.i == 0:
            return IndexError
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.i > 0:
            return self.prefixsmall[-1]
        else:
            return None
