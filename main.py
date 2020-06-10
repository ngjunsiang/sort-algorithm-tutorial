from tests import testSort


def bubbleSort(array):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using bubble sort algorithm.
    '''
    if len(array) == 0:
        return array
    sorted_index = len(array) - 1
    while sorted_index > 0:
        for i in range(1, sorted_index + 1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
        sorted_index -= 1
    return array


def insertionSort(array):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using insertion sort algorithm.
    '''
    size = len(array) - 1
    sorted_index = 0
    while sorted_index < size:
        el = array.pop(sorted_index + 1)
        inserted = False
        i = 0
        while i <= sorted_index:
            if not inserted and el <= array[i]:
                array.insert(i, el)
                inserted = True
            i += 1
        if not inserted:
            if sorted_index >= size:
                array.append(el)
            else:
                array.insert(sorted_index + 1, el)
        sorted_index += 1
    return array


def mergeSort(array):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using merge sort algorithm.
    '''
    def merge(left, right):
        array = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                el = left.pop(0)
            else:
                el = right.pop(0)
            array.append(el)
        return array + left + right
    
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    sortedarray = merge(left, right)
    return sortedarray


def quickSort(array):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using quick sort algorithm.
    '''
    if len(array) <= 1:
        return array
    # pick last element as pivot
    pivot = array[-1]
    ltearray = []
    gtarray = []
    for el in array[:-1]:
        if el <= pivot:
            ltearray.append(el)
        else:
            gtarray.append(el)
    ltearray = quickSort(ltearray)
    gtarray = quickSort(gtarray)
    return ltearray + [pivot] + gtarray