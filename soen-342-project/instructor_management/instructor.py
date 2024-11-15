# instructor_management/instructor.py

from utils.utils import append_csv, read_csv, write_csv

class Instructor:
    def __init__(self, name, specialization, cities):
        self.name = name
        self.specialization = specialization
        self.cities = cities

    @staticmethod
    def register(name, specialization, cities):
        # Read existing instructors to determine the latest ID
        instructors = read_csv('data/instructors.csv')
        
        if instructors:
            # Ensure that all existing IDs are valid and non-empty
            valid_ids = [instructor['id'] for instructor in instructors if instructor.get('id', '').startswith('I')]
            
            if valid_ids:
                # Sort IDs and get the last one in numeric order
                last_id = sorted(valid_ids, key=lambda x: int(x[1:]))[-1]
                new_id = f"I{int(last_id[1:]) + 1:03}"  # Increment the numeric part of the ID
            else:
                new_id = "I001"  # Start with 'I001' if no valid IDs exist
        else:
            new_id = "I001"  # Start with 'I001' if the file is empty

        # Append instructor data with the new ID
        append_csv('data/instructors.csv', {
            'id': new_id,
            'name': name,
            'specialization': specialization,
            'cities': ','.join(cities)
        }, fieldnames=['id', 'name', 'specialization', 'cities'])
        
        print(f"Instructor {name} registered successfully with ID {new_id}.")

    @staticmethod
    def assign_instructor_to_lesson(lesson_id, instructor_name):
        # Read the current lessons and instructors
        lessons = read_csv('data/lessons.csv')
        instructors = read_csv('data/instructors.csv')
        
        # Find the instructor by name
        instructor = next((inst for inst in instructors if inst['name'] == instructor_name), None)
        if not instructor:
            print("Error: Instructor not found.")
            return
        
        # Find the lesson by ID
        lesson = next((lesson for lesson in lessons if lesson['id'] == lesson_id), None)
        if not lesson:
            print("Error: Lesson not found.")
            return
        
        # Assign the instructor to the lesson
        lesson['instructor'] = instructor['id']
        lesson['is_public'] = 'True'  # Make lesson public once assigned

        # Write updated lessons back to the CSV file
        write_csv('data/lessons.csv', lessons, fieldnames=lessons[0].keys())
        
        print(f"Instructor {instructor_name} assigned to lesson {lesson_id} successfully.")
