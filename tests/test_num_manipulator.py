import number_challenges.num_manipulator as nm


manipulator = nm.NumManipulator()


def test_decimal_to_octal():
    decimal = 20.89
    octal = 24.707534

    assert manipulator.decimal_to_octal(decimal) == octal


def test_reverse_number():
    number = 3467
    reversed_number = 7643
    assert manipulator.reverse_integer(number) == reversed_number


def test_print_fibonacci():
    target_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    assert manipulator.fibonacci_series() == target_sequence