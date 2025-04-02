import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parent.parent)) 
from SUM.sum_solution import compute


def test_compute_with_valid_input() -> None:

    assert compute(1,2) == 3
    assert compute(0, 100) == 100
    assert compute(100, 99) == 199
