# instructor_management/instructor.py
from utils.utils import append_csv

class Instructor:
    def __init__(self, name, specialization, cities):
        self.name = name
        self.specialization = specialization
        self.cities = cities

    @staticmethod
    def register(name, specialization, cities):
        append_csv('data/instructors.csv', {
            'name': name,
            'specialization': specialization,
            'cities': ','.join(cities)
        }, fieldnames=['name', 'specialization', 'cities'])
        print("Instructor registered successfully.")
