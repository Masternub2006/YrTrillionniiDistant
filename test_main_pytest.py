import pytest
from main import calculate_average

def test_empty_list():
    assert calculate_average([]) is None
def test_positive_numbers():
    assert calculate_average([1, 2, 3]) == 2.0
def test_negative_numbers():
    assert calculate_average([-1, -2, -3]) == -2.0
def test_mixed_numbers():
    assert calculate_average([-1, 2, -3, 4]) == 0.5