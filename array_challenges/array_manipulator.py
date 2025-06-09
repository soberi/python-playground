# To be placed in ArrayManipulator:
#   Find the largest and the smallest number in a given array.
#   Find the second largest number in the integer array.
#   Print array in reverse order.
#   Insert an element at the end of an array.
#   Merge two sorted arrays into a single sorted array.

class ArrayManipulator:

    # Find the largest and the smallest number in a given array.
    def largest_smallest_number(self, array):
        largest = max(array)
        smallest = min(array)

        return largest, smallest
    
    # Find the largest and the smallest number in a given array.
    def largest_smallest_loop(self, array):
        largest = array[0]
        smallest = array[0]

        for i in array:
            if i > largest:
                largest = i

        for i in array:
            if i < smallest:
                smallest = i

        return largest, smallest


    def second_largest_number(self, array):
        sorted_array = sorted(array)
        second_largest = sorted_array[-2]

        return second_largest


    def reverse_array(self, array):
        # Print array in reverse order.
        array.reverse()

        for i in array:
            print(i)

        return array
    

    def merge_sorted_array(self, array1, array2):
        
        merged_list = sorted(array1 + array2)
        return merged_list
