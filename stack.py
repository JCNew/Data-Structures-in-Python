class Stack:
    def __init__(self, values, limit: int = 10, *args):
        self.stack = [val for val in args] + values
        self.limit = limit

    def __str__(self):
        print("_____")
        for i in self.stack:
            print(f"| {i} |")
        return "-----"

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
