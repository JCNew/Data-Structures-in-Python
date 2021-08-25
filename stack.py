# STACK IMPLEMENTATION

'''Time complexities:
        Inserting: O(1),
        Removing: O(1)
        (Searching and accessing are not possible unless the values are on top, in that case it's O(1))
'''


class Stack:
    def __init__(self, values: list, limit: int = 10):
        self.__stack = values
        self.limit = limit

    def __len__(self):
        # Allows the len() function to be invoked using the object instead of the property
        return len(self.__stack)

    def __iter__(self):
        # Allows it to be iterated using the object
        for item in self.__stack:
            yield item

    def __str__(self):
        # Returns a representation of the linked list including available spots
        stack_vals = []
        for item in reversed(self.__stack):
            stack_vals.append(f"| {item} |")
        return ("|   |\n" * (self.limit - len(self.__stack))) + "\n".join(stack_vals)

    def is_empty(self) -> bool:
        # Checks wether the stack is empty or not
        if not self.__stack:
            return True
        else:
            return False

    def push(self, value):
        # Pushes an element into the end (top) of the stack
        if stack.limit > len(self.__stack):
            self.__stack.append(value)

    def pop(self):
        # Removes element from the top of the stack
        return self.__stack.pop()

    def peek(self):
        # Allows checking what the element on top is
        return self.__stack[-1]
