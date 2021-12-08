from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(data, node.left)
        elif data['id'] > node.data['id']:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(data, node.right)
        else:  # if equal, meaning it is already there
            return

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id , self.root)

    def _search_recursive(self, blog_post_id, node):
        # if node.left is None and node.right is None:
        #     return False
        if blog_post_id == node.data['id']:
            return node.data
        if blog_post_id < node.data['id'] and node.left is not None:
            if blog_post_id == node.left.data['id']:
                return node.left.data
            else:
                return self._search_recursive(blog_post_id, node.left)
        elif blog_post_id > node.data['id'] and node.right is not None:
            if blog_post_id == node.right.data['id']:
                return node.right.data
            else:
                return self._search_recursive(blog_post_id, node.right)
        return False

