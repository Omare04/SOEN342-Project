# main.py
from client_management.client import Client
from client_management.booking import Booking
from instructor_management.instructor import Instructor
from lesson_management.offering import Offering
from admin_management.admin import Admin

def main():
    while True:
        print("\nMenu:")
        print("1. Register Client")
        print("2. Create Booking")
        print("3. Register Instructor")
        print("4. Create Lesson")
        print("5. Assign Instructor to Lesson")
        print("6. View Offerings")
        print("7. Cancel Booking")
        print("8. Cancel Offering")
        print("9. Register Guardian")
        print("10. Exit")

        choice = input("Enter choice: ")
        
        if choice == "1":  # Register Client
            name = input("Enter client name: ")
            age = int(input("Enter client age: "))
            guardian_name = None
            if age < 18:
                guardian_name = input("Enter guardian's name (required for underage clients): ")
            Client.register(name, age, guardian_name)
            
        elif choice == "2":  # Create Booking
            client_name = input("Enter client name: ")
            offering_id = input("Enter offering ID: ")
            Booking.create_booking(client_name, offering_id)
            
        elif choice == "3":  # Register Instructor
            name = input("Enter instructor name: ")
            specialization = input("Enter specialization: ")
            cities = input("Enter cities (comma-separated): ").split(",")
            Instructor.register(name, specialization, cities)
            
        elif choice == "4":  # Create Lesson
            lesson_type = input("Enter lesson type: ")
            location = input("Enter location: ")
            schedule = input("Enter schedule ID: ")
            Admin.create_lesson(lesson_type, location, schedule)
            
        elif choice == "5":  # Assign Instructor to Lesson
            lesson_id = input("Enter lesson ID: ")
            instructor_name = input("Enter instructor name: ")
            Instructor.assign_instructor_to_lesson(lesson_id, instructor_name)
            
        elif choice == "6":  # View Offerings
            Client.view_offerings()
            
        elif choice == "7":  # Cancel Booking
            client_name = input("Enter client name: ")
            offering_id = input("Enter offering ID: ")
            Booking.cancel_booking(client_name, offering_id)
            
        elif choice == "8":  # Cancel Offering
            offering_id = input("Enter offering ID: ")
            Admin.cancel_offering(offering_id)
            
        elif choice == "9":  # Register Guardian
            guardian_name = input("Enter guardian name: ")
            minor_name = input("Enter minor's name: ")
            minor_age = int(input("Enter minor's age: "))
            Client.register_guardian(guardian_name, minor_name, minor_age)
            
        elif choice == "10":  # Exit
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
