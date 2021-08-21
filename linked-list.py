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

# INSERTING A NEW ELEMENT IMPLEMENTATION


class InsertableLinkedList(LinkedList):
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


# TESTING INSERTING
linked_list2 = InsertableLinkedList([1, 3, 5, 7])
linked_list2.add_in_head(Node(2))
linked_list2.add_end(Node(10))

for node in linked_list2:
    print(node, end=" -> ")
print(None)
