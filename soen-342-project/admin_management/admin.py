# admin_management/admin.py
import uuid
from utils.utils import append_csv, read_csv, write_csv

class Admin:
    @staticmethod
    def create_lesson(lesson_type, location, schedule):
        lesson = {
            'id': str(uuid.uuid4()),
            'lesson_type': lesson_type,
            'location': location,
            'schedule': schedule,
            'instructor': None,
            'is_public': False
        }
        append_csv('data/lessons.csv', lesson, fieldnames=['id', 'lesson_type', 'location', 'schedule', 'instructor', 'is_public'])
        print("Lesson created successfully.")

# instructor_management/instructor.py
def assign_instructor_to_lesson(lesson_id, instructor_name):
    lessons = read_csv('data/lessons.csv')
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if lesson and lesson['instructor'] is None:
        lesson['instructor'] = instructor_name
        lesson['is_public'] = True
        write_csv('data/lessons.csv', lessons, fieldnames=lesson.keys())
        print("Instructor assigned and lesson is now an offering.")
    else:
        print("Error: Lesson already has an instructor or does not exist.")

def cancel_offering(offering_id):
        bookings = read_csv('data/bookings.csv')
        # Check if there are no bookings for this offering
        if any(b['offering_id'] == offering_id for b in bookings):
            print("Cannot cancel offering; clients have already booked.")
            return

        # Remove offering from lessons
        lessons = read_csv('data/lessons.csv')
        lessons = [l for l in lessons if l['id'] != offering_id]
        write_csv('data/lessons.csv', lessons, fieldnames=['id', 'lesson_type', 'location', 'schedule', 'instructor', 'is_public'])
        print("Offering canceled successfully.")
