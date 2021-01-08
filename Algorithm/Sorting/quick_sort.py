def quick_sort(l):
    """
    Quick Sort Implementation.
    Time O(nlogn) Run.
    O(logn) space complexity.
    """
    less = []
    equal = []
    greater = []

    if len(l) > 1:
        pivot = l[0]
        for x in l:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quick_sort(less) + equal + quick_sort(greater)  # + operator to join lists

    else:
        return l


# A more efficient solution, less verbose
def quick_sort2(l):
    """
    Quick Sort Implementation.
    Time O(nlogn) Run.
    O(logn) space complexity.
    """
    if len(l) <= 1:
        return l

    pivot  = l[len(l) // 2]
    left   = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right  = [x for x in l if x > pivot]

    return quick_sort2(left) + middle + quick_sort2(right)


print(quick_sort2([12, 4, 5, 6, 7, 3, 1, 15, -1, -100, 38, 0, 1]))
