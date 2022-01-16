# patients bmi calculator
BMI calculator

Data
`[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]`


Output:

`[{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI Range (kg/m2)': 32.83061454806607, 'BMI Category': 'Moderately obese', 'Health risk': 'Medium risk'}, {'Gender': '
Male', 'HeightCm': 161, 'WeightKg': 85, 'BMI Range (kg/m2)': 32.79194475521777, 'BMI Category': 'Moderately obese', 'Health risk': 'Medium risk'}, {'Gender': 'Male', 'HeightCm': 180, 'Wei
ghtKg': 77, 'BMI Range (kg/m2)': 23.76543209876543, 'BMI Category': 'Normal weight', 'Health risk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMI Range (kg/m2)':
 22.49963710262738, 'BMI Category': 'Normal weight', 'Health risk': 'Low risk'}, {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'BMI Range (kg/m2)': 31.11111111111111, 'BMI Categor
y': 'Moderately obese', 'Health risk': 'Medium risk'}, {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'BMI Range (kg/m2)': 29.402273297715947, 'BMI Category': 'Overweight', 'Health
 risk': 'Enhanced risk'}]`

Overweight Patients: 4