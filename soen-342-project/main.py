from threading import Lock

from client_management.client import Client
from client_management.booking import Booking
from instructor_management.instructor import Instructor
from lesson_management.offering import Offering
from admin_management.admin import Admin
from utils.utils import read_csv

reader_lock = Lock()
writer_lock = Lock()
active_readers = 0


def start_reading():
    """Allow multiple readers to access concurrently, blocking writers."""
    global active_readers
    with reader_lock:
        active_readers += 1
        if active_readers == 1:
            writer_lock.acquire()


def stop_reading():
    """Release access when a reader finishes."""
    global active_readers
    with reader_lock:
        active_readers -= 1
        if active_readers == 0:
            writer_lock.release()


def start_writing():
    """Ensure only one writer operates at a time, blocking all readers."""
    writer_lock.acquire()


def stop_writing():
    """Release the writer lock."""
    writer_lock.release()


def admin_menu(admin_id):
    while True:
        print("\nAdmin Menu:")
        print("1. Create Lesson")
        print("2. View All Offerings")
        print("3. Cancel Offering")
        print("4. View Lessons")
        print("5. Delete Lesson")
        print("6. View All Instructors")
        print("7. Delete Instructor")
        print("8. View All Clients")
        print("9. Delete Client")
        print("10. Delete Guardian")
        print("11. Logout")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":  # Create Lesson
                start_writing()
                try:
                    lesson_type = input("Enter lesson type: ").strip()
                    location_id = input("Enter location ID: ").strip()
                    schedule_id = input("Enter schedule ID: ").strip()
                    Admin.create_lesson(lesson_type, location_id, schedule_id)
                finally:
                    stop_writing()

            elif choice == "2":  # View All Offerings
                start_reading()
                try:
                    Admin.view_all_offerings()
                finally:
                    stop_reading()

            elif choice == "3":  # Cancel Offering
                start_writing()
                try:
                    offering_id = input("Enter offering ID: ").strip()
                    Admin.cancel_offering(offering_id)
                finally:
                    stop_writing()

            elif choice == "4":  # View Lessons
                start_reading()
                try:
                    Admin.view_lessons()
                finally:
                    stop_reading()

            elif choice == "5":  # Delete Lesson
                start_writing()
                try:
                    lesson_id = input("Enter lesson ID: ").strip()
                    Admin.delete_lesson(lesson_id)
                finally:
                    stop_writing()

            elif choice == "6":  # View All Instructors
                start_reading()
                try:
                    Admin.view_all_instructors()
                finally:
                    stop_reading()

            elif choice == "7":  # Delete Instructor
                start_writing()
                try:
                    instructor_id = input("Enter instructor ID: ").strip()
                    Admin.delete_instructor(instructor_id)
                finally:
                    stop_writing()

            elif choice == "8":  # View All Clients
                start_reading()
                try:
                    Admin.view_all_clients()
                finally:
                    stop_reading()

            elif choice == "9":  # Delete Client
                start_writing()
                try:
                    client_id = input("Enter client ID: ").strip()
                    Admin.remove_client(client_id)
                finally:
                    stop_writing()

            elif choice == "10":  # Delete Guardian
                start_writing()
                try:
                    guardian_id = input("Enter guardian ID: ").strip()
                    Admin.delete_guardian(guardian_id)
                finally:
                    stop_writing()

            elif choice == "11":  # Logout
                print("Logging out.")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


def client_menu(client_id):
    while True:
        print("\nClient Menu:")
        print("1. Create Booking")
        print("2. View All Offerings")
        print("3. View My Details")
        print("4. View My Bookings")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            start_writing()
            try:
                print("\nAvailable Offerings:")
                Client.view_available_offerings()
                offering_id = input("Enter the Offering ID to book: ").strip()
                if offering_id:
                    Booking.create_booking(client_id, offering_id)
                else:
                    print("Invalid Offering ID. Please try again.")
            finally:
                stop_writing()

        elif choice == "2":
            start_reading()
            try:
                Client.view_available_offerings()
            finally:
                stop_reading()

        elif choice == "3":
            start_reading()
            try:
                Client.view_client_details(client_id)
            finally:
                stop_reading()

        elif choice == "4":
            start_reading()
            try:
                Client.view_client_bookings(client_id)
            finally:
                stop_reading()

        elif choice == "5":
            print("Logging out.")
            break

        else:
            print("Invalid choice. Please try again.")


def instructor_menu(instructor_id):
    while True:
        print("\nInstructor Menu:")
        print("1. View Assigned Offerings")
        print("2. Assign Myself to an Offering")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            start_reading()
            try:
                Instructor.view_assigned_offerings(instructor_id)
            finally:
                stop_reading()

        elif choice == "2":
            start_writing()
            try:
                Client.view_available_offerings()
                offering_id = input("Enter the Offering ID to book: ").strip()
                Instructor.assign_to_offering(offering_id, instructor_id)
            finally:
                stop_writing()

        elif choice == "3":
            print("Logging out.")
            break


def login():
    while True:
        print("\nLogin Menu:")
        print("1. Admin Login")
        print("2. Client Login")
        print("3. Instructor Login")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_id = input("Enter admin ID: ")
            admins = read_csv('data/users.csv')
            admin = next((a for a in admins if a['user_id'] == admin_id and a['user_type'] == "Admin"), None)
            if admin:
                print(f"Admin {admin['name']} logged in successfully.")
                return admin_id, "Admin"
        elif choice == "2":
            client_id = input("Enter client ID: ")
            clients = read_csv('data/users.csv')
            client = next((c for c in clients if c['user_id'] == client_id and c['user_type'] == "Client"), None)
            if client:
                print(f"Client {client['name']} logged in successfully.")
                return client_id, "Client"
        elif choice == "3":
            instructor_id = input("Enter instructor ID: ")
            instructors = read_csv('data/users.csv')
            instructor = next((i for i in instructors if i['user_id'] == instructor_id and i['user_type'] == "Instructor"), None)
            if instructor:
                print(f"Instructor {instructor['name']} logged in successfully.")
                return instructor_id, "Instructor"
        elif choice == "5":
            print("Exiting system. Goodbye!")
            return None, None
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        logged_in_user, user_role = login()
        if not logged_in_user:
            break

        if user_role == "Admin":
            admin_menu(logged_in_user)
        elif user_role == "Client":
            client_menu(logged_in_user)
        elif user_role == "Instructor":
            instructor_menu(logged_in_user)


if __name__ == "__main__":
    main()
