def bubble_sort(coll: list):
    """
    Bubble Sort Implementation.
    (n-1) + (n-2) + (n-3) + ... + 3 + 2 + 1 = n(n-1)/2 => O(n^2)
    Time O(n^2) run.
    O(1) space complexity.
    """
    for i in range(len(coll) - 1, 0, -1):
        for j in range(i):
            if coll[j] > coll[j + 1]:
                coll[j], coll[j + 1] = coll[j + 1], coll[j]


def bubble_sort_optimize(coll: list):
    """
    Optimized version of bubble-sort.
    At any iteration, if the list is ordered, there is no swap.
    If there was no swap, the algorithm finishes.
    Time O(n^2) run in the worst case, O(n) for ordered input.
    O(1) space complexity.
    """
    has_swapped = True

    while has_swapped:
        has_swapped = False
        for j in range(len(coll) - 1):
            if coll[j] > coll[j + 1]:
                coll[j], coll[j + 1] = coll[j + 1], coll[j]
                has_swapped = True


l = [99, 440, 6, 2, 1, 50, 63, 87, 283, 0, -100, 3]
bubble_sort(l)
print(l)
