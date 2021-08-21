# LINKED LIST NODES IMPLEMENTATION

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# REGULAR LINKED LIST IMPLEMENTATION


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            # Converting the value with index 0 into the list's head
            head = Node(nodes.pop(0))
            self.head = head
            current = head
            # Iterating and setting every node after that to the current value's next property
            for node in nodes:
                current.next = Node(node)
                current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

# CREATING A LINKED LIST


linked_list1 = LinkedList([1, 3, 5, 7])

# TESTING ITERATION

for node in linked_list1:
    print(node, end=" -> ")
print(None)
