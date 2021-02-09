# A linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Utility function to print a linked list
def print_list(msg, head):
    print(msg, end=': ')
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")


# Iteratively reverse a linked list from position m to n
def reverse(head, m, n):
    prev = None
    curr = head

    # 1. Skip the first m nodes.
    i = 1
    while curr is not None and i < m:
        prev = curr
        curr = curr.next
        i = i + 1

    # prev now points to position the (m-1)'th node
    # curr now points to position the m'th node

    start = curr
    end = None

    # 2. Traverse and reverse the sub-list from position m to n
    while curr is not None and i <= n:
        # Take note of the next node
        next = curr.next

        # move the 'curr' node onto the 'end'
        curr.next = end
        end = curr

        # move to the next node
        curr = next
        i = i + 1

    # start points to the m'th node
    # end now points to the n'th node
    # curr now points to the (n+1)'th node

    # 3. Fix the pointers and return the head node.
    start.next = curr
    if prev is None:  # when m = 1 (prev is None)
        head = end
    else:
        prev.next = end

    return head


def reverse2(head, m, n):
    if m == n:
        return head
    curr = head
    prev = None
    i = 0
    while curr and i < m - 1:  # skip m-1 elements
        prev = curr
        curr = curr.next
        i += 1

    first_node = prev  # saving prev to attach the first node of reversed list
    last_node = curr  # saving curr node to attach with the last node of reversed list

    i = 0
    next = None
    while curr and i < n - m + 1:  # actual reversal
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    #  at the end of this 'while':
    # 'prev' will be the last item to be reversed, hence first after reversing
    # 'curr' will be the first item after the reversal portion
    # the pointers within the reversed sub-list changed within the 'while'
    # the pointers before and after will be defined below

    if first_node is not None:  # linking this node with the first node of reversed list
        first_node.next = prev
    else:
        head = prev

    last_node.next = curr  # linking this node with the last node of reversed list
    return head


if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    (m, n) = (2, 4)

    print_list("\nOriginal Linked List", head)
    head = reverse2(head, m, n)
    print_list("Reversed Linked List", head)
