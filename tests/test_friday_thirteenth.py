import pytest
import challenges.friday_thirteenth as ft

# Parameters passed to function ar mm-yyyy
has_friday_thirteen = (6, 2025)
no_friday_thirteen = (5, 2025)
error_wrong_input = ("a", "b")

def test_has_friday_thirteen():
    assert ft.has_friday_thirteenth(
        has_friday_thirteen[0],
        has_friday_thirteen[1]
        ) == True

def test_no_friday_thirteen():
    assert ft.has_friday_thirteenth(
       no_friday_thirteen[0],
       no_friday_thirteen[1] 
    ) == False

def test_wrong_input():
    with pytest.raises(TypeError) as e:

        ft.has_friday_thirteenth(
        error_wrong_input[0],
        error_wrong_input[1] 
        )