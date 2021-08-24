# LINKED LIST NODES IMPLEMENTATION

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node with value {self.value}"


# SINGLY LINKED LIST IMPLEMENTATION

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

    def __str__(self):
        return " -> ".join(str(node) for node in self)

    def __len__(self):
        return len(tuple(iter(self)))

    def convert_to_node(self, value):
        return Node(value)

    def insert_in_head(self, node):
        if not isinstance(node, Node):
            node = self.convert_to_node(node)
        node.next = self.head
        self.head = node

    def insert_in_tail(self, node):
        if not isinstance(node, Node):
            node = self.convert_to_node(node)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def insert_in_nth(self, index, node):
        if not (0 <= index <= len(self)):
            raise IndexError("List index out of range")
        if not isinstance(node, Node):
            node = self.convert_to_node(node)
        current = self.head
        if self.head is None:
            self.head = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def remove_nth(self, index):
        if not (0 <= index <= len(self)):
            raise IndexError("List index out of range")
        current = self.head
        deleted_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                current = current.next
            deleted_node = current.next
            current.next = current.next.next
        return deleted_node.value

    def is_empty(self):
        return not self.head

    def search(self, value):
        current = self.head
        while current.next is not None:
            if current.value == value:
                return value
            current = current.next
        return False
