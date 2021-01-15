class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """
        Returns list of strings, width, height,
        and horizontal coordinate of the root.
        """
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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

    def bfs(self):
        """
        BFS Implementation.
        Top-to-bottom, Scans each level from left to right.
        Time O(n) run.
        :return: A List with nodes values, BFS style.
        """

        current_node = self.root
        answer = []
        children = []

        while current_node:
            answer.append(current_node)
            if current_node.left:
                children.append(current_node.left)

            if current_node.right:
                children.append(current_node.right)

            if children:
                current_node = children.pop(0)
            else:
                break

        return [x.value for x in answer]

    def bfs_rec(self, queue, answer):
        if not queue:
            return answer

        current = queue.pop(0)
        answer.append(current)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        self.bfs_rec(queue, answer)

        return [x.value for x in answer]

    def dfs_inorder(self, node):
        if node is None:
            return
        self.dfs_inorder(node.left)
        print(node.value)
        self.dfs_inorder(node.right)

    def dfs_preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)

    def dfs_postorder(self, node):
        if node is None:
            return
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node.value)


# TESTING
# ########## FIRST BSF ####################
# b = BinarySearchTree()
# b.insert(9)
# b.insert(4)
# b.insert(20)
# b.insert(1)
# b.insert(6)
# b.insert(15)
# b.insert(170)
# b.root.display() if b.root else None
# print()  # line break
# print(b.bfs())

# usual print
# print(b)

########### BFS_REC PRINT ##################

b = BinarySearchTree()
b.insert(9)
b.insert(4)
b.insert(20)
b.insert(1)
b.insert(6)
b.insert(15)
b.insert(170)
b.root.display() if b.root else None
 
########### BFS INORDER PREODER POSTORDER ##################

print()  # line break
# print(b.bfs_rec([b.root], []))
b.dfs_inorder(b.root)
print()  # line break
b.dfs_preorder(b.root)
print()  # line break
b.dfs_postorder(b.root)
