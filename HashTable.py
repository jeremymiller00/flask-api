from Node import Node
from Data import Data

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for k in key:
            hash_value += ord(k)
            hash_value = (hash_value * ord(k)) % self.table_size
        return hash_value

    def add_key_value_pair(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node

            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            
            if key == node.data.key:
                return node.data.value
        return None

    def print_table(self):
        print("{")
        for i, v in enumerate(self.hash_table):
            if v is not None:
                ll_string = ""
                node = v
                if node.next_node:
                    while node.next_node:
                        ll_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " ---> "
                        )
                        node = node.next_node
                    ll_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " ---> "
                    )
                    print(f"    [{i}] {ll_string}")
                else:
                    print(f"    [{i}] {v.data.key} : {v.data.value}")
            else:
                print(f"    [{i}] {v}")
        print("}")