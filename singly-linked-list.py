# LINKED LIST NODES IMPLEMENTATION

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# REGULAR LINKED LIST IMPLEMENTATION


class SinglyLinkedList:
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

    def add_in_head(self, node):
        node.next = self.head
        self.head = node

    def add_end(self, node):
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
