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
