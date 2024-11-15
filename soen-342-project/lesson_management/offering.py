# lesson_management/offering.py
from utils.utils import read_csv, write_csv, append_csv

class Offering:
    @staticmethod
    def manage_lesson(lesson_id, action, **kwargs):
        lessons = read_csv('data/lessons.csv')
        if action == "create":
            append_csv('data/lessons.csv', kwargs, fieldnames=kwargs.keys())
            print("Lesson created successfully.")
        elif action == "modify":
            lesson = next((lesson for lesson in lessons if lesson['id'] == lesson_id), None)
            if lesson:
                lesson.update(kwargs)
                write_csv('data/lessons.csv', lessons, fieldnames=lessons[0].keys())
                print("Lesson modified successfully.")
        elif action == "delete":
            lessons = [lesson for lesson in lessons if lesson['id'] != lesson_id]
            write_csv('data/lessons.csv', lessons, fieldnames=lessons[0].keys())
            print("Lesson deleted successfully.")
