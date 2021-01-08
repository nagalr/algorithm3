def merge_sort(l):
    """
    Merge Sort Implementation.
    Time O(nlogn) run.
    O(n) space complexity
    :param l: List
    :return: None, sorts inline.
    """
    if len(l) > 1:
        mid = len(l) // 2  # rounds division to int
        left = l[:mid]
        right = l[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                l[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                l[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1


l = [6, 5, 3, 1, 8, 7, 2, 4]
merge_sort(l)
print(l)
