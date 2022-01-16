import pytest
from src.bmicalculator import BMICalculator


@pytest.fixture
def example_people_data():
    obj = BMICalculator()
    obj.calculate_bmi()
    print(obj.get_bmi_data())