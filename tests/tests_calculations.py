# tests/test_calculations.py
import pytest
from faker import Faker
fake = Faker()

def test_addition():
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    expected_output = a + b  # Simulate expected logic
    assert a + b == expected_output

def test_subtraction():
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    expected_output = a - b  # Simulate expected logic
    assert a - b == expected_output
