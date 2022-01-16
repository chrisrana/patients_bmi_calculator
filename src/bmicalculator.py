import json
from src.utility import timing


class BMICalculator:
    BMI_HEALTH_RISK_MAP = {}

    def __init__(self):
        self.bmi_patients_data_calculated = []
        self.overweight = 0
        self.no_of_records = 0

    @staticmethod
    def read_json_data():
        f = open('data/patient_bmi_data.json')
        #f = open('data/data.json')
        data = json.load(f)
        return data

    @staticmethod
    def get_bmi(bmi_patient_data):
        return bmi_patient_data["WeightKg"]/(bmi_patient_data["HeightCm"]/100*bmi_patient_data["HeightCm"]/100)

    @staticmethod
    def get_bmi_category(patient_bmi):
        if patient_bmi <= 18.4:
            return "Underweight"
        elif 18.5 <= patient_bmi <= 24.9:
            return "Normal weight"
        elif 25 <= patient_bmi <= 29.9:
            return "Overweight"
        elif 30 <= patient_bmi <= 34.9:
            return "Moderately obese"
        elif 35 <= patient_bmi <= 39.9:
            return "Severely obese"
        elif patient_bmi >= 40:
            return "Very severely obese"

    @staticmethod
    def get_health_risk(patient_bmi: float) -> str:
        if patient_bmi <= 18.4:
            return "Malnutrition risk"
        elif 18.5 <= patient_bmi <= 24.9:
            return "Low risk"
        elif 25 <= patient_bmi <= 29.9:
            return "Enhanced risk"
        elif 30 <= patient_bmi <= 34.9:
            return "Medium risk"
        elif 35 <= patient_bmi <= 39.9:
            return "High risk"
        elif patient_bmi >= 40:
            return "Very high risk"

    @timing
    def calculate_bmi(self):
        """
        BMI(kg/m2) = mass(kg) / height(m)2
        :return:
        """
        bmi_patients_data = self.read_json_data()
        overweight = 0
        for cnt, item in enumerate(bmi_patients_data):
            bmi = self.get_bmi(item)
            if bmi >= 25:
                overweight = overweight+1
            bmi_patients_data[cnt]["BMI Range (kg/m2)"] = bmi
            bmi_patients_data[cnt]["BMI Category"] = self.get_bmi_category(bmi)
            bmi_patients_data[cnt]["Health risk"] = self.get_health_risk(bmi)
        self.bmi_patients_data_calculated = bmi_patients_data
        self.overweight = overweight
        self.no_of_records = len(bmi_patients_data)

    def get_bmi_data(self):
        return self.bmi_patients_data_calculated

    def get_overweight(self):
        return self.overweight

    def get_records_count(self):
        return self.no_of_records
