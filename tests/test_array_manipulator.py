import array_challenges.array_manipulator as am

manipulator = am.ArrayManipulator()

test_array = [10, 20, 4, 28, 85, 73]

def test_largest_smallest():
    largest = 85
    smallest = 4
    assert manipulator.largest_smallest_number(test_array) == (largest, smallest)


def test_largest_smallest_loop():
    largest = 85
    smallest = 4
    assert manipulator.largest_smallest_loop(test_array) == (largest, smallest)


def test_second_largest_number():
    second_largest = 73
    assert manipulator.second_largest_number(test_array) == second_largest


def test_reverse_array():
    reversed_array = [73, 85, 28, 4, 20, 10]
    assert manipulator.reverse_array(test_array) == reversed_array


def test_merge_array():
    second_array = [3, 56, 24, 66, 12]
    merged_array = [3, 4, 10, 12, 20, 24, 28, 56, 66, 73, 85]

    assert manipulator.merge_sorted_array(test_array, second_array) == merged_array