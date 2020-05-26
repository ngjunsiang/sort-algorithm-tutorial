from random import shuffle
import copy


def testSort(sortFunction, **kwargs):
    '''
    Author: 
    Date: 

    Tests to verify that sort function works correctly.
    
    Requirements:
    1. Output array has same number of elements as input array
    2. Each element in the output array is smaller than or equal to the
       next element
    3. Each element in the input must be in the output.
       There must be no elements in the output that are not in the input.
    '''
    count = {'passed': 0,
             'failed': 0,
             }

    def same_length(input_array, output_array):
        return len(input_array) == len(output_array)
    
    def correct_order(output_array):
        for i in range(0, len(output_array) - 1):
            if not output_array[i] <= output_array[i + 1]:
                return False
        return True
    
    def same_identity(input_array, output_array):
        temp_array = copy.copy(output_array)
        for each in input_array:
            if each in temp_array:
                temp_array.remove(each)
        if len(temp_array) != 0:
            return False
        else:
            return True

    # Test with arrays of size 0 to 100
    for size in range(0, 101):
        input_array = [i for i in range(size)]
        shuffle(input_array)
        output_array = sortFunction(input_array)

        print(f'Testing {sortFunction.__name__}:')
        if same_length(input_array, output_array):
            result = 'passed'
        else:
            result = 'failed'
        count[result] += 1
        print(f'size {size}: length check {result}')

        if correct_order(output_array):
            result = 'passed'
        else:
            result = 'failed'
        count[result] += 1
        print(f'size {size}: order check {result}')

        if same_identity(input_array, output_array):
            result = 'passed'
        else:
            result = 'failed'
        count[result] += 1
        print(f'size {size}: identity check {result}')
    print(f'tests passed: {count["passed"]}, failed: {count["failed"]}')