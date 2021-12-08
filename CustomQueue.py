from Node import Node


class CustomQueque:
    """
    Add to tail, pull from head
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        if self.head is None:
            return None
        output = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return output
