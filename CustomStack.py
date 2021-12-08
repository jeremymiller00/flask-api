from Node import Node


class CustomStack:
    """
    Add to head, pull from head
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            return None
        output = self.head
        self.head = self.head.next_node
        return output
