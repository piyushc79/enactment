# Given an unsorted array of integers, sort the array into a
# wave like array. An array arr[0..n-1] is sorted in wave
# form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...


def sort_wave_form(array):
    n = len(array)
    for i in range(0, n, 2):
        if i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
        if i < n-1 and array[i] < array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

if __name__ == '__main__':
    arr = [1, 4, 2, 6, 8, 9, 3]
    print 'Array {}'.format(arr)
    sort_wave_form(arr)
    print 'Wave Form sorted Array {}'.format(arr)
