# tests/test_calculations.py
import pytest

def test_addition(calculator):
    result = calculator.commands['add'].execute(10, 5)
    assert result == 15

def test_subtraction(calculator):
    result = calculator.commands['subtract'].execute(10, 5)
    assert result == 5

def test_multiplication(calculator):
    result = calculator.commands['multiply'].execute(10, 5)
    assert result == 50

def test_division(calculator):
    result = calculator.commands['divide'].execute(10, 5)
    assert result == 2

def test_division_by_zero(calculator):
    result = calculator.commands['divide'].execute(10, 0)
    assert result == "Error: Divide by zero"
