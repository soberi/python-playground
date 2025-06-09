import number_challenges.num_manipulator as nm

decimal = 20.89
octal = 24.707534

manipulator = nm.NumManipulator()

def test_decimal_to_octal():
    assert manipulator.decimal_to_octal(decimal) == octal