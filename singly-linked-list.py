# LINKED LIST NODES IMPLEMENTATION

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node with value {self.value}"


# SINGLY LINKED LIST IMPLEMENTATION
'''Time complexities:
        Searching, Accessing: O(n) (same concept since you have to iterate and can't use indexes),
        Inserting: O(1),
        Removing: O(1),
        '''


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
        # Makes sure for loops are usable in this data structure
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        # Using the print() function allows it to display a representation of the list
        return " -> ".join(str(node) for node in self)

    def __len__(self):
        # Allows the len() function to be used
        return len(tuple(iter(self)))

    def convert_to_node(self, value):
        # Converts the values into nodes where necessary
        return Node(value)

    def insert_in_head(self, node):
        # Inserts a node in self.head, can also be implemented using the insert_in_nth() method
        if not isinstance(node, Node):
            node = self.convert_to_node(node)
        node.next = self.head
        self.head = node

    def insert_in_tail(self, node):
        # Inserts a node in the last slot, can also be implemented using the insert_in_nth() method
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
        # Inserts a node on the nth position
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
        # Removes node in nth position, can also be used to remove head or tail
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
        # Checks if the linked list is empty
        return not self.head

    def access(self, value):
        # Looks for a value inside the list and returns its node if it is found
        current = self.head
        while current.next is not None:
            if current.value == value:
                return current
            current = current.next
        return False
