import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_example_case():
    """Test the primary example case from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive_numbers():
    """Test a list with only non-positive numbers (zeros and negatives)."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_streak_at_beginning():
    """Test a list where the longest streak is at the beginning."""
    assert longest_positive_streak([4, 5, 6, 0, 1, 2]) == 3

def test_streak_at_end():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, 6]) == 4

def test_multiple_streaks_longest_in_middle():
    """Test a list with multiple positive streaks to ensure the longest is returned."""
    assert longest_positive_streak([1, 0, 2, 2, 0, 3, 3, 3, 0, 4]) == 3

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([10]) == 1

def test_single_non_positive_number():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-5]) == 0

def test_all_same_positive_numbers():
    """Test a list with all identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3
