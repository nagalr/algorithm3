class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __repr__(self):
        """
        Overwrites the default __repr__
        Refers to print_tree method
        to print the tree values
        """
        return str(self.print_tree(self.root))

    def print_tree(self, curr_node):
        """
        Recursively traverse the a tree and prints its Nodes value
        Takes O(n) time.
        """
        if curr_node is None:
            return
        self.print_tree(curr_node.left)
        print(curr_node.value)
        self.print_tree(curr_node.right)

    def insert(self, value):
        """
        Insert a value wrapped with a Node into a tree.
        Takes O(log n) time.
        """
        if not self.root:
            self.root = Node(value)
            return
        curr = self.root
        while curr:
            if curr.value > value and curr.left:
                curr = curr.left
            elif curr.value < value and curr.right:
                curr = curr.right
            else:
                break
        if curr.value >= value:
            curr.left = Node(value)
        elif curr.value < value:
            curr.right = Node(value)

    def lookup(self, value):
        """
        Lookup for a Node with a given value.
        Takes O(log n) time. 
        """
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return curr_node
            elif curr_node.value > value:
                curr_node = curr_node.left
            elif curr_node.value < value:
                curr_node = curr_node.right

        return None
