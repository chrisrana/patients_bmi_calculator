import pytest
import unittest
from src.bmicalculator import BMICalculator


def test_bmi_calculation():
    obj = BMICalculator()
    obj.calculate_bmi()
    assert obj.get_records_count() == 6


def test_validate_no_of_overweight():
    obj = BMICalculator()
    obj.calculate_bmi()
    assert obj.get_overweight() == 4


def test_validate_bmi_category():
    obj = BMICalculator()
    obj.calculate_bmi()
    updated_records = obj.get_bmi_data()
    assert updated_records[0]['BMI Category'] == 'Moderately obese'



