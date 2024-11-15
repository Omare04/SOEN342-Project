# client_management/client.py
from utils.utils import append_csv, initialize_csv, read_csv

class Client:
    def __init__(self, name, age, guardian_name=None):
        self.name = name
        self.age = age
        self.guardian_name = guardian_name

    @staticmethod
    def register(name, age, guardian_name=None):
        # Check if the client is underage
        if age < 18 and not guardian_name:
            print("Error: Underage clients must have a guardian.")
            return
        
        # Initialize clients.csv with headers if it doesn't exist
        initialize_csv('data/clients.csv', ['name', 'age', 'guardian_name'])
        
        # Append client data
        append_csv('data/clients.csv', {
            'name': name,
            'age': age,
            'guardian_name': guardian_name
        }, fieldnames=['name', 'age', 'guardian_name'])
        print("Client registered successfully.")

    @staticmethod
    def view_offerings():
        offerings = read_csv('data/lessons.csv')
        for offering in offerings:
            # Check if 'is_public' key exists and is set to 'True'
            if offering.get('is_public', 'False') == 'True':
                print(f"Offering ID: {offering['id']}, Type: {offering['lesson_type']}, Location: {offering['location']}")
            else:
                print(f"Offering ID: {offering['id']} is not available to the public.")
                
    @staticmethod
    def register_guardian(guardian_name, minor_name, minor_age):
        if minor_age >= 18:
            print("Error: Guardians are only required for clients under 18.")
            return
        
        guardian = {'guardian_name': guardian_name, 'minor_name': minor_name, 'minor_age': minor_age}
        initialize_csv('data/guardian.csv', ['guardian_name', 'minor_name', 'minor_age'])
        append_csv('data/guardian.csv', guardian, fieldnames=['guardian_name', 'minor_name', 'minor_age'])
        print("Guardian registered successfully.")
