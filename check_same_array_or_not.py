# Given two given arrays of equal length, the task is to find
# if given arrays are equal or not. Two arrays are said to be
# equal if both of them contain same set of elements, arrang-
# -ements (or permutation) of elements may be different though.


def is_same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    frequency = reduce(lambda d, c: d.update({c: d.get(c, 0) + 1}) or d, arr1, {})

    for a in arr2:
        if not frequency.has_key(a):
            return False
        if not frequency.get(a):
            return False
        frequency[a] -= 1
    return True


if __name__ == '__main__':
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
    print 'Are {} and {} same? {}'.format(arr1, arr2, is_same(arr1, arr2))