import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parent.parent)) 
from SUM.sum_solution import compute


def test_compute_with_valid_input():

    assert compute(1,2) == 3
    assert compute(0, 100) == 100
    assert compute(100, 99) == 199

def test_x_out_of_range():
    with pytest.raises(ValueError) as error_mesg:
        compute(-1, 100)

    assert str(error_mesg.value) == "x must be between 0 and 100"

    with pytest.raises(ValueError) as error_mesg:
        compute(101, 100)

    assert str(error_mesg.value) == "x must be between 0 and 100"


def test_y_out_of_range_lower():
    with pytest.raises(ValueError) as error_mesg:
        compute(58, -2)

    assert str(error_mesg.value) == "y must be between 0 and 100"


    with pytest.raises(ValueError) as error_mesg:
        compute(58, 101)

    assert str(error_mesg.value) == "y must be between 0 and 100"


def test_x_and_y_out_of_range():
    with pytest.raises(ValueError) as error_mesg:
        compute(-2, -2)

    assert str(error_mesg.value) == "x must be between 0 and 100"


    with pytest.raises(ValueError) as error_mesg:
        compute(101, 101)

    assert str(error_mesg.value) == "x must be between 0 and 100"

