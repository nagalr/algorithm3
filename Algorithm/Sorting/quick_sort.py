def quick_sort(l):
    """
    Quick Sort Implementation.
    Time O(nlogn) Run.
    O(logn) space complexity.
    :param l: List
    :return: None
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


print(quick_sort([12, 4, 5, 6, 7, 3, 1, 15, -1, -100, 38, 0, 1]))
