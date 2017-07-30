def partition(unsorted_array1, left, right):
    import ipdb; ipdb.set_trace()
    lm = left+1
    rm = right
    pivot = unsorted_array1[left]
    while True:
        while lm < right and unsorted_array1[lm] <= pivot:
            lm += 1
        while rm > left and unsorted_array1[rm] >= pivot:
            rm -= 1
        if lm >= rm:
            break
        else:
            temp = unsorted_array1[lm]
            unsorted_array1[lm] = unsorted_array1[rm]
            unsorted_array1[rm] = temp
    temp = unsorted_array1[left]
    unsorted_array1[left] = unsorted_array1[rm]
    unsorted_array1[rm] = temp
    return rm


def quick_select(unsorted_array2, left, right, k):

    if k not in range(left, right+1):
        return None

    if left == right:
        if k == left:
            return unsorted_array2[left]
        else:
            return None
    split = partition(unsorted_array2, left, right)
    length = split - left + 1

    if length == k:
        return unsorted_array2[k]
    elif length > k:
        return quick_select(unsorted_array2, left, split-1, k)
    else:
        return quick_select(unsorted_array2, split+1, right, k-length)


def find_median(unsorted_array):

    length = len(data)

    if length % 2:
        return quick_select(unsorted_array, 0, length-1, (length/2)+1)
    else:
        m1 = quick_select(unsorted_array, 0, length-1, length/2)
        m2 = quick_select(unsorted_array, 0, length-1, (length/2)+1)

        if m1 is not None and m2 is not None:
            return (m1+m2)/2.0
        return None


if __name__ == '__main__':
    data = [7, 1, 3, 8, 5, 6, 2, 4]
    # data = [3, 2, 6, 4, 1, 5, 7, 9, 8]
    print find_median(data)