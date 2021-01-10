def linear_search(l, item):
    """
    Liner Search Implementation.
    Time O(n) run.
    O(1) space complexity, finds in place.
    :param l: A List
    :param item: Item from the List or N/a (-1).
    :return:the founded index of the wanted item.
    """
    for i in range(len(l)):
        if item == l[i]:
            return i
    return -1


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 32]
item = 5
print(linear_search(l, item))
