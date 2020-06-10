from random import shuffle
from tests import testSort


class Counter:
    '''Helper class for counting number of operations'''
    def __init__(self, algorithm):
        self.algo = algorithm
        pass
    
    def __repr__(self):
        return f"Counter('{self.algo}')"
    
    def increment(self, num):
        '''Increase counter by num'''
        pass

    def count(self):
        '''Get counter value'''
        pass

class CSV:
    '''Class for exporting data'''
    def __init__(self, filename):
        self.filename = filename
        pass
    
    def __repr__(self):
        return f"CSV('{self.filename}')"

    def write(self, row, mode='a'):
        '''Write a row to CSV file'''
        pass

def bubbleSort(array, counter=None):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using bubble sort algorithm.
    '''
    if len(array) == 0:
        return array
    sorted_index = len(array) - 1
    noswaps = False
    while not noswaps and sorted_index > 0:
        noswaps = True
        for i in range(1, sorted_index + 1):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                noswaps = False
                if counter is not None:
                    counter.increment()
            if counter is not None:
                counter.increment()
        # return array early if no swaps made (i.e. sorted)
        if noswaps:
            return array
        sorted_index -= 1
    return array


def insertionSort(array, counter=None):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using insertion sort algorithm.
    '''
    # Use a function to exit for loop early
    def first_index(array, el):
        '''Returns the first index of array that is <= el'''
        for i in range(0, len(array)):
            if counter is not None:
                counter.increment()
            if el < array[i]:
                return i
        return None  # if no index found

    size = len(array) - 1
    for sorted_index in range(size):
        el = array.pop(sorted_index + 1)
        insert_index = first_index(array[:sorted_index + 1], el)
        if insert_index is None:
            if sorted_index >= size:
                array.append(el)
            else:
                array.insert(sorted_index + 1, el)
        else:
            array.insert(insert_index, el)
        if counter is not None:
            counter.increment()
    return array


def mergeSort(array, counter=None):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using merge sort algorithm.
    '''
    def merge(left, right):
        # preallocate array to minimise array appending
        array = [None] * (len(left) + len(right))
        l_size, r_size = len(left), len(right)
        a = l = r = 0  # array indices
        while l < l_size and r < r_size:
            if counter is not None:
                counter.increment()
            if left[l] <= right[r]:
                array[a] = left[l]
                a += 1
                l += 1
            else:
                array[a] = right[r]
                a += 1
                r += 1
        if l < l_size:
            array[a:] = left[l:]
        if r < r_size:
            array[a:] = right[r:]
        return array
    
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left, counter)
    right = mergeSort(right, counter)

    sortedarray = merge(left, right)
    return sortedarray


def quickSort(array, counter=None):
    '''
    Author: Ng Jun Siang
    Date: 20200610

    Sorts array elements in ascending order (smallest to largest)
    using quick sort algorithm.
    '''
    # speed up creation of ltearray and gtarray
    # using list comprehensions (avoid append)
    if len(array) <= 1:
        return array
    pivot = array[-1]
    ltearray = [el for el in array[:-1] if el <= pivot]
    gtarray = [el for el in array[:-1] if el > pivot]
    if counter is not None:
        counter.increment(len(ltearray))
        counter.increment(len(gtarray))
    ltearray = quickSort(ltearray, counter)
    gtarray = quickSort(gtarray, counter)
    return ltearray + [pivot] + gtarray


if __name__ == "__main__":
    for algo in (bubbleSort,     # each iteration will
                 insertionSort,  # assign an algorithm
                 mergeSort,      # to count ops for
                 quickSort,
                 ):
        algorithm = algo.__name__
        csvdata = CSV(f'{algorithm}.csv')
        # Count ops for n in multiples of 100,
        # up to 4000
        for n in range(0, 100, 4100):
            ctr = Counter(algorithm)  # initialise a counter
            array = [n for n in range(n)]
            shuffle(array)
            algo(array, ctr)  # pass counter to algorithm
            ops_count = ctr.count()  # extract ops count
            csvdata.write([n, ops_count])  # write row to CSV

# When you have 4 CSV files, one for each algorithm,
# import them into Google Sheets and plot a line graph
# of all 4
