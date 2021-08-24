class Stack:
    def __init__(self, values: list, limit: int = 10, *args):
        self.__stack = values + [val for val in args]
        self.limit = limit

    def __len__(self):
        return len(self.__stack)

    def __iter__(self):
        for item in self.__stack:
            yield item
        free_spaces = self.limit - len(self.__stack)
        yield str(free_spaces) + " free spaces"

    def __str__(self):
        stack_vals = []
        for item in reversed(self.__stack):
            stack_vals.append(f"| {item} |")
        return ("|   |\n" * (self.limit - len(self.__stack))) + "\n".join(stack_vals)

    def is_empty(self) -> bool:
        if not self.__stack:
            return True
        else:
            return False

    def push(self, value):
        if stack.limit > len(self.__stack):
            self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]
