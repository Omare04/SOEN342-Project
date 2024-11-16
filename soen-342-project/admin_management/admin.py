import uuid
from utils.utils import append_csv, read_csv, write_csv, initialize_csv

class Admin:
    @staticmethod
    def create_lesson(lesson_type, location_id, schedule_id):
        # Initialize `lessons.csv` if it doesn't exist
        initialize_csv('data/lessons.csv', ['lesson_id', 'lesson_type', 'location_id', 'schedule_id', 'instructor_id', 'is_public'])
        
        # Create a new lesson
        lesson = {
            'lesson_id': str(uuid.uuid4()),
            'lesson_type': lesson_type,
            'location_id': location_id,
            'schedule_id': schedule_id,
            'instructor_id': None,
            'is_public': 'False'  # Lessons are private by default until an instructor is assigned
        }
        append_csv('data/lessons.csv', lesson, fieldnames=['lesson_id', 'lesson_type', 'location_id', 'schedule_id', 'instructor_id', 'is_public'])
        print("Lesson created successfully.")

    @staticmethod
    def assign_instructor_to_lesson(lesson_id, instructor_id):
        # Load lessons and validate
        lessons = read_csv('data/lessons.csv')
        lesson = next((l for l in lessons if l['lesson_id'] == lesson_id), None)
        if not lesson:
            print("Error: Lesson not found.")
            return
        
        # Check if instructor is already assigned
        if lesson['instructor_id']:
            print("Error: Lesson already has an instructor assigned.")
            return
        
        # Assign instructor
        lesson['instructor_id'] = instructor_id
        lesson['is_public'] = 'True'  # Mark lesson as public
        write_csv('data/lessons.csv', lessons, fieldnames=lessons[0].keys())
        print(f"Instructor {instructor_id} assigned to lesson {lesson_id}.")

    @staticmethod
    def cancel_offering(offering_id):
        # Load bookings and ensure no bookings exist for the offering
        bookings = read_csv('data/bookings.csv')
        if any(b['offering_id'] == offering_id for b in bookings):
            print("Cannot cancel offering; clients have already booked.")
            return

        # Remove offering from lessons
        lessons = read_csv('data/lessons.csv')
        lessons = [l for l in lessons if l['lesson_id'] != offering_id]
        write_csv('data/lessons.csv', lessons, fieldnames=['lesson_id', 'lesson_type', 'location_id', 'schedule_id', 'instructor_id', 'is_public'])
        print(f"Offering {offering_id} canceled successfully.")

    @staticmethod
    def view_lessons():
        # Display all lessons
        lessons = read_csv('data/lessons.csv')
        if not lessons:
            print("No lessons found.")
            return

        print("Available Lessons:")
        for lesson in lessons:
            print(f"Lesson ID: {lesson['lesson_id']}, Type: {lesson['lesson_type']}, Location ID: {lesson['location_id']}, Schedule ID: {lesson['schedule_id']}, Instructor ID: {lesson.get('instructor_id', 'None')}, Public: {lesson['is_public']}")

    @staticmethod
    def delete_lesson(lesson_id):
        # Load and remove lesson by ID
        lessons = read_csv('data/lessons.csv')
        updated_lessons = [l for l in lessons if l['lesson_id'] != lesson_id]

        if len(updated_lessons) == len(lessons):
            print("Error: Lesson not found.")
            return

        write_csv('data/lessons.csv', updated_lessons, fieldnames=['lesson_id', 'lesson_type', 'location_id', 'schedule_id', 'instructor_id', 'is_public'])
        print(f"Lesson {lesson_id} deleted successfully.")

    @staticmethod
    def update_lesson(lesson_id, **kwargs):
        # Update lesson details by ID
        lessons = read_csv('data/lessons.csv')
        lesson = next((l for l in lessons if l['lesson_id'] == lesson_id), None)
        if not lesson:
            print("Error: Lesson not found.")
            return

        # Update fields
        for key, value in kwargs.items():
            if key in lesson:
                lesson[key] = value

        write_csv('data/lessons.csv', lessons, fieldnames=lessons[0].keys())
        print(f"Lesson {lesson_id} updated successfully.")
        
    @staticmethod
    def remove_client(client_id):
        """
        Remove a client by their ID (Admin-only operation).
        """
        clients = read_csv('data/clients.csv')
        updated_clients = [c for c in clients if int(c['client_id']) != int(client_id)]

        if len(clients) == len(updated_clients):
            print("Error: Client not found.")
        else:
            write_csv('data/clients.csv', updated_clients, fieldnames=['client_id', 'name', 'phone', 'email', 'age', 'guardian_id'])
            print(f"Client with ID {client_id} removed successfully.")

    @staticmethod
    def view_all_clients():
        """
        View all clients (Admin-only operation).
        """
        clients = read_csv('data/clients.csv')
        if not clients:
            print("No clients found.")
            return

        print("\nAll Registered Clients:")
        print(f"{'ID':<10}{'Name':<20}{'Phone':<15}{'Email':<30}{'Age':<5}{'Guardian ID':<15}")
        print("=" * 95)
        for client in clients:
            print(f"{client['client_id']:<10}{client['name']:<20}{client['phone']:<15}{client['email']:<30}{client['age']:<5}{client['guardian_id'] or 'N/A':<15}")
        print("=" * 95)
        
    @staticmethod
    def delete_instructor(instructor_id):
        # Remove instructor from the database
        instructors = read_csv('data/instructors.csv')
        updated_instructors = [inst for inst in instructors if inst['instructor_id'] != instructor_id]

        if len(updated_instructors) == len(instructors):
            print("Error: Instructor not found.")
            return

        write_csv('data/instructors.csv', updated_instructors, fieldnames=['instructor_id', 'name', 'phone', 'specialization'])
        print("Instructor deleted successfully.")

    @staticmethod
    def view_all_instructors():
        """
        View all registered instructors (Admin-only operation).
        Combines data from `users.csv` and `instructors.csv`.
        """
        # Read both `users.csv` and `instructors.csv`
        users = read_csv('data/users.csv')
        instructors = read_csv('data/instructors.csv')

        if not instructors:
            print("No instructors found.")
            return

        # Print the table header
        print("\nAll Registered Instructors:")
        print(f"{'ID':<10}{'Name':<20}{'Phone':<15}{'Specialization':<30}")
        print("=" * 75)

        # Combine data from both files
        for instructor in instructors:
            try:
                # Use the actual column name from the CSV file
                instructor_id = instructor['instructor_id FK(user_id)']
                
                # Find the user data corresponding to the instructor
                user = next((u for u in users if u['user_id'] == instructor_id), None)
                if user:
                    print(f"{instructor_id:<10}{user['name']:<20}{user['phone']:<15}{instructor['specialization']:<30}")
                else:
                    print(f"Error: No matching user found for instructor ID {instructor_id}")
            except KeyError as e:
                print(f"Error: Missing field {e} in instructor data: {instructor}")

        print("=" * 75)

    @staticmethod
    def view_all_clients():
        """
        View all registered clients (Admin-only operation).
        Combines data from `users.csv` and `clients.csv`.
        """
        # Read both `users.csv` and `clients.csv`
        users = read_csv('data/users.csv')
        clients = read_csv('data/clients.csv')

        if not clients:
            print("No clients found.")
            return

        # Print the table header
        print("\nAll Registered Clients:")
        print(f"{'ID':<10}{'Name':<20}{'Phone':<15}{'Email':<30}{'Age':<5}{'Guardian ID':<15}")
        print("=" * 95)

        # Combine data from both files
        for client in clients:
            try:
                # Use the correct column name for `client_id` and find the user details
                client_id = client['client_id FK(user_id)']
                user = next((u for u in users if u['user_id'] == client_id), None)

                if user:
                    print(f"{client_id:<10}{user['name']:<20}{user['phone']:<15}{user['email']:<30}{client['age']:<5}{client.get('guardian_id', 'N/A'):<15}")
                else:
                    print(f"Error: No matching user found for client ID {client_id}")
            except KeyError as e:
                print(f"Error: Missing field {e} in client data: {client}")

        print("=" * 95)

    @staticmethod
    def delete_guardian(guardian_id):
        """
        Remove a guardian by their ID (Admin-only operation).
        """
        guardians = read_csv('data/guardians.csv')
        users = read_csv('data/users.csv')  # To ensure the corresponding user is also handled

        # Find and remove the guardian from `guardians.csv`
        updated_guardians = [g for g in guardians if int(g['guardian_id FK(user_id)']) != int(guardian_id)]
        if len(guardians) == len(updated_guardians):
            print("Error: Guardian not found.")
            return

        # Update the `guardians.csv` file
        write_csv('data/guardians.csv', updated_guardians, fieldnames=['guardian_id FK(user_id)', 'client_id', 'age'])

        # Also handle the corresponding user in `users.csv`
        updated_users = [u for u in users if u['user_id'] != guardian_id]
        write_csv('data/users.csv', updated_users, fieldnames=['user_id', 'name', 'phone', 'email', 'user_type'])

        print(f"Guardian with ID {guardian_id} removed successfully.")

    @staticmethod
    def view_all_offerings():
        """
        View all offerings in the `offerings.csv` file with FK validation.
        """
        # Read all necessary CSV files
        offerings = read_csv('data/offerings.csv')
        locations = read_csv('data/locations.csv')
        schedules = read_csv('data/schedules.csv')
        instructors = read_csv('data/instructors.csv')
        rooms = read_csv('data/rooms.csv')
        users = read_csv('data/users.csv')  # To fetch instructor names

        if not offerings:
            print("No offerings found.")
            return

        # Print the table header
        print("\nAll Offerings:")
        print(f"{'Offering ID':<15}{'Lesson Type':<20}{'Private':<10}{'Available':<10}{'Location':<25}{'Schedule':<20}{'Instructor':<20}{'Room':<15}")
        print("=" * 130)

        # Display offerings data
        for offering in offerings:
            try:
                # Validate and fetch related data
                location = next((loc for loc in locations if loc['location_id'] == offering['location_id']), None)
                schedule = next((sch for sch in schedules if sch['schedule_id'] == offering['schedule_id']), None)
                instructor = next((inst for inst in instructors if inst['instructor_id FK(user_id)'] == offering['instructor_id']), None)
                room = next((rm for rm in rooms if rm['room_id'] == offering['room_id']), None)

                # Determine the instructor name
                if offering['is_available'].lower() == 'true':  # If offering is available
                    instructor_name = "----"
                else:
                    instructor_name = "Unknown Instructor"
                    if instructor:
                        user = next((u for u in users if u['user_id'] == instructor['instructor_id FK(user_id)']), None)
                        instructor_name = user['name'] if user else "Unknown Instructor"

                # Construct display values
                location_name = location['name'] if location else "Unknown Location"
                schedule_info = f"{schedule['start_date']} to {schedule['end_date']} ({schedule['day']})" if schedule else "Unknown Schedule"
                room_info = f"{room['room_number']} ({room['location_id']})" if room else "Unknown Room"

                # Print the offering details
                print(f"{offering['offering_id']:<15}{offering['lesson_type']:<20}{offering['is_private']:<10}{offering['is_available']:<10}{location_name:<25}{schedule_info:<20}{instructor_name:<20}{room_info:<15}")
            except KeyError as e:
                print(f"Error: Missing field {e} in offering data: {offering}")

        print("=" * 130)
