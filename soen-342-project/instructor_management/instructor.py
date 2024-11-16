from utils.utils import append_csv, read_csv, write_csv, initialize_csv
from User import User

class Instructor(User):
    
    def __init__(self, user_id, name, phone, email, specialization):
        super().__init__(user_id, name, phone, email)  # Inherit common attributes
        self.specialization = specialization

    @staticmethod
    def register(name, phone, email, specialization):
        """
        Register a new instructor.
        """
        # Generate unique instructor ID
        instructors = read_csv('data/instructors.csv')
        instructor_id = f"I{len(instructors) + 1:03}"

        # Register in `users.csv` as an `Instructor`
        User.register_user(instructor_id, name, phone, email, "Instructor")

        # Initialize `instructors.csv` if it doesn't exist
        initialize_csv('data/instructors.csv', ['instructor_id', 'specialization'])

        # Append instructor-specific data to `instructors.csv`
        append_csv('data/instructors.csv', {
            'instructor_id': instructor_id,
            'specialization': specialization
        }, fieldnames=['instructor_id', 'specialization'])
        print(f"Instructor {name} registered successfully with ID {instructor_id}.")

    @staticmethod
    def assign_to_offering(offering_id, instructor_id):
        """
        Assign the instructor to an offering. The instructor can only assign themselves.
        """
        # Read the data from CSV files
        instructors = read_csv('data/instructors.csv')
        offerings = read_csv('data/offerings.csv')

        # Validate instructor ID
        instructor = next((inst for inst in instructors if inst['instructor_id FK(user_id)'] == instructor_id), None)
        if not instructor:
            print("Error: Instructor not found.")
            return

        # Validate offering
        offering = next((off for off in offerings if off['offering_id'] == offering_id), None)
        if not offering:
            print("Error: Offering not found.")
            return

        # Ensure the offering is available
        if offering.get('is_available', 'True') == 'False':
            print(f"Error: Offering {offering_id} is not available for assignment.")
            return

        # Assign instructor to the offering
        if instructor_id == instructor['instructor_id FK(user_id)']:
            offering['instructor_id'] = instructor_id
            offering['is_available'] = 'False'  # Mark the offering as unavailable
            write_csv('data/offerings.csv', offerings, fieldnames=offerings[0].keys())
            print(f"Instructor {instructor_id} successfully assigned to offering {offering_id}.")
        else:
            print("Error: You can only assign yourself to an offering.")


    @staticmethod
    def view_assigned_offerings(instructor_id):
        """
        View all offerings assigned to this instructor.
        """
        # Read required data
        instructors = read_csv('data/instructors.csv')
        offerings = read_csv('data/offerings.csv')
        locations = read_csv('data/locations.csv')
        schedules = read_csv('data/schedules.csv')

        # Validate instructor ID
        instructor = next((inst for inst in instructors if inst['instructor_id FK(user_id)'] == instructor_id), None)
        if not instructor:
            print("Error: Instructor not found.")
            return

        # List offerings assigned to the instructor
        assigned_offerings = [off for off in offerings if off['instructor_id'] == instructor_id]
        if not assigned_offerings:
            print("No offerings assigned to this instructor.")
            return

        # Print the table header
        print("\nAssigned Offerings:")
        print(f"{'Offering ID':<15}{'Lesson Type':<20}{'Location':<25}{'Schedule':<30}")
        print("=" * 90)

        # Display assigned offerings
        for offering in assigned_offerings:
            try:
                # Fetch location and schedule details
                location = next((loc for loc in locations if loc['location_id'] == offering['location_id']), None)
                schedule = next((sch for sch in schedules if sch['schedule_id'] == offering['schedule_id']), None)

                location_name = location['name'] if location else "Unknown Location"
                schedule_info = f"{schedule['start_date']} to {schedule['end_date']} ({schedule['day']})" if schedule else "Unknown Schedule"

                # Print offering details
                print(f"{offering['offering_id']:<15}{offering['lesson_type']:<20}{location_name:<25}{schedule_info:<30}")
            except KeyError as e:
                print(f"Error: Missing field {e} in offering data: {offering}")

        print("=" * 90)
