# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bmicalculator import BMICalculator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Calculating BMI of patients')
    obj = BMICalculator()
    obj.calculate_bmi()
    print("No. of Records: {}".format(len(obj.get_bmi_data())))
    print("Update Records:{}".format(obj.get_bmi_data()))
    print("Overweight Patients: {}".format(obj.get_overweight()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
