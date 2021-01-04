class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        """
        A node in a doubly-linked list.
        """
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):  # 'toString' Impl
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        """
        Create a new doubly linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        result = []
        curr = self.head
        while curr:
            result.append(repr(curr))  # using ListNode 'repr'
            curr = curr.next
        return '[' + ', '.join(result) + ']'

    def prepend(self, data=None):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        new_head = ListNode(data, next=self.head, prev=None)
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data, next=None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data, next=None, prev=curr)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        """
        Unlink an element contains `key` from the list.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if curr and curr.prev:
            curr.prev.next = curr.next
        if curr and curr.next:
            curr.next.prev = curr.prev
        if curr and curr is self.head:
            self.head = curr.next
        if curr:
            curr.next = None
            curr.prev = None

    def remove2(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        elem = self.find(key)
        if not elem:
            return
        self.remove_item(elem)

    def remove_item(self, node: ListNode):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        if self.head is None or self.head.next is None:
            return

        curr_node = self.head
        prev_node = self.head.prev
        next_node = self.head.next

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            curr_node.prev = next_node

            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
