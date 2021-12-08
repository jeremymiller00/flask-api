from Node import Node

class LinkedList:
    """
    Keeps track of head
    """
    def __init__(self):
        self.head=None
        self.last_node=None

    def __str__(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += "None"
        return ll_string

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_list(self):
        l = []
        if self.head is not None:
            node = self.head
            while node:
                l.append(node.data)
                node = node.next_node
        return l

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data['id'] == int(user_id):
                return node.data
            node = node.next_node
        return None




# ll = LinkedList()
# ll.insert_beginning("data1")
# ll.insert_beginning("data2")
# ll.insert_end("dataend")
# ll.insert_beginning("data3")
# ll.insert_beginning("data4")
# ll.insert_end("dataend2")
# ll.insert_beginning("data5")
# ll.insert_beginning("data6")
# ll.insert_end("dataend3")
# ll.insert_beginning("data7")
# ll.insert_beginning("data8")
# ll.insert_end("dataend4")

# # node4 = Node("data4", None)
# # node3 = Node("data3", node4)
# # node2 = Node("data2", node3)
# # node1 = Node("data1", node2)

# # ll.head = node1
# print(ll)