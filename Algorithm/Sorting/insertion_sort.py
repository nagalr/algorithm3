def insertion_sort(l):
    """
    Insertion Sort Implementation
    Time O(n) run.
    O(1) space complexity.
    """
    # finds the next item to insert
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            item = l[i]

            # moves the item to its right location
            for j in range(i, 0, -1):
                if item < l[j - 1]:
                    l[j], l[j - 1] = l[j - 1], l[j]


l = [2, 1, 1, -10, 10, -1, 0, 11, -1, 111, -111, -1, 0, 1000]
insertion_sort(l)
print(l)
