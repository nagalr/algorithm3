class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return str(self.value)


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        curr = self.first
        result = []
        while curr:
            result.append(curr.value)
            curr = curr.next
        return str(result)

    def enqueue(self, value):
        new_node = Node(value)
        if self.first:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        else:
            self.first = new_node
            self.last = new_node
            self.length = 1

    def dequeue(self):
        if self.first:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp
        else:
            return None

    def peek(self):
        return self.first

    def isEmpty(self):
        return self.length == 0
