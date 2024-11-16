from client_management.client import Client
from client_management.booking import Booking
from instructor_management.instructor import Instructor
from lesson_management.offering import Offering
from admin_management.admin import Admin
from utils.utils import read_csv


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
                lesson_type = input("Enter lesson type: ").strip()
                location_id = input("Enter location ID: ").strip()
                schedule_id = input("Enter schedule ID: ").strip()
                Admin.create_lesson(lesson_type, location_id, schedule_id)

            elif choice == "2":  # View All Offerings
                Admin.view_all_offerings()

            elif choice == "3":  # Cancel Offering
                offering_id = input("Enter offering ID: ").strip()
                Admin.cancel_offering(offering_id)

            elif choice == "4":  # View Lessons
                Admin.view_lessons()

            elif choice == "5":  # Delete Lesson
                lesson_id = input("Enter lesson ID: ").strip()
                Admin.delete_lesson(lesson_id)

            elif choice == "6":  # View All Instructors
                Admin.view_all_instructors()

            elif choice == "7":  # Delete Instructor
                instructor_id = input("Enter instructor ID: ").strip()
                Admin.delete_instructor(instructor_id)

            elif choice == "8":  # View All Clients
                Admin.view_all_clients()

            elif choice == "9":  # Delete Client
                client_id = input("Enter client ID: ").strip()
                Admin.remove_client(client_id)

            elif choice == "10":  # Delete Guardian
                guardian_id = input("Enter guardian ID: ").strip()
                Admin.delete_guardian(guardian_id)

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
        print("4. View My Bookings")  # New menu option
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nAvailable Offerings:")
            Client.view_available_offerings()  
            offering_id = input("Enter the Offering ID to book: ").strip()
            if offering_id:
                Booking.create_booking(client_id, offering_id)
            else:
                print("Invalid Offering ID. Please try again.")

        elif choice == "2":
            Client.view_available_offerings()  # Simply view available offerings

        elif choice == "3":
            Client.view_client_details(client_id)  # View client's personal details

        elif choice == "4":  # View bookings for the client
            Client.view_client_bookings(client_id)

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
            Instructor.view_assigned_offerings(instructor_id)
        elif choice == "2":
            Client.view_available_offerings()
            offering_id = input("Enter the Offering ID to book: ").strip()
            Instructor.assign_to_offering(offering_id, instructor_id)
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

        if choice == "1":  # Admin Login
            admin_id = input("Enter admin ID: ")
            admins = read_csv('data/users.csv')
            admin = next((a for a in admins if a['user_id'] == admin_id and a['user_type'] == "Admin"), None)
            if admin:
                print(f"Admin {admin['name']} logged in successfully.")
                return admin_id, "Admin"
        elif choice == "2":  # Client Login
            client_id = input("Enter client ID: ")
            clients = read_csv('data/users.csv')
            client = next((c for c in clients if c['user_id'] == client_id and c['user_type'] == "Client"), None)
            if client:
                print(f"Client {client['name']} logged in successfully.")
                return client_id, "Client"
        elif choice == "3":  # Instructor Login
            instructor_id = input("Enter instructor ID: ")
            instructors = read_csv('data/users.csv')
            instructor = next((i for i in instructors if i['user_id'] == instructor_id and i['user_type'] == "Instructor"), None)
            if instructor:
                print(f"Instructor {instructor['name']} logged in successfully.")
                return instructor_id, "Instructor"
        elif choice == "5":  # Exit
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
