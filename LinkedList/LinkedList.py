class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):  # 'toString' Impl
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):  # 'toString' Impl
        result = []
        curr = self.head
        while curr:
            result.append(repr(curr))  # using ListNode 'repr'
            curr = curr.next
        return '[' + ', '.join(result) + ']'

    def prepend(self, data=None):
        self.head = ListNode(data, self.head)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data, None)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr and prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse2(self):
        """
        Reverse the list using accessory list.
        Takes O(n) time, O(n) space.
        """
        l2 = SinglyLinkedList()
        curr = self.head
        while curr:
            l2.prepend(curr)
            curr = curr.next
        return l2

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def reverse3(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev
