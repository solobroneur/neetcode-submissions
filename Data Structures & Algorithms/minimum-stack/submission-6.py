class MinStack:

    def __init__(self):
        self.values = list()
        self.minimums = list()
        

    def push(self, val: int) -> None:
        self.values.append(val)

        if not self.minimums:
            self.minimums.append(val)
        else:
            minimum = self.minimums[-1]
            self.minimums.append(min(val, minimum))
        

    def pop(self) -> None:
        self.values.pop()
        self.minimums.pop()
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
        
