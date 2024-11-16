from utils.utils import append_csv, read_csv, write_csv, initialize_csv

class Offering:
    @staticmethod
    def is_offering_available(location_id, room_id, schedule_id):
        """
        Check if the offering is available based on location, room, and schedule.
        """
        # Read offerings and rooms to verify availability
        offerings = read_csv('data/offerings.csv')
        rooms = read_csv('data/rooms.csv')

        # Check if the room is available
        room = next((r for r in rooms if int(r['room_id']) == int(room_id) and r['location_id'] == location_id), None)
        if not room or room['is_available'] != 'True':
            print(f"Error: Room {room_id} in Location {location_id} is not available.")
            return False

        # Check if there's an existing offering with the same room and schedule
        for offering in offerings:
            if (
                int(offering['room_id']) == int(room_id) and
                offering['schedule_id'] == schedule_id and
                offering['is_available'] == 'True'
            ):
                print(f"Error: Room {room_id} is already booked for Schedule {schedule_id}.")
                return False

        return True

    @staticmethod
    def create_offering(lesson_type, is_private, location_id, schedule_id, instructor_id, room_id):
        """
        Create a new offering after checking its availability.
        """
        # Initialize `offerings.csv` if it doesn't exist
        initialize_csv('data/offerings.csv', ['offering_id', 'lesson_type', 'is_private', 'is_available', 'location_id', 'schedule_id', 'instructor_id', 'room_id'])
        offerings = read_csv('data/offerings.csv')
        offering_id = f"O{len(offerings) + 1:03}"  # Generate unique offering ID

        # Check if the offering is available
        is_available = Offering.is_offering_available(location_id, room_id, schedule_id)

        # Create the offering
        offering = {
            'offering_id': offering_id,
            'lesson_type': lesson_type,
            'is_private': str(is_private),
            'is_available': str(is_available),
            'location_id': location_id,
            'schedule_id': schedule_id,
            'instructor_id': instructor_id,
            'room_id': room_id
        }

        # Append the offering if available
        append_csv('data/offerings.csv', offering, fieldnames=['offering_id', 'lesson_type', 'is_private', 'is_available', 'location_id', 'schedule_id', 'instructor_id', 'room_id'])
        if is_available:
            print(f"Offering {offering_id} created successfully and is available.")
        else:
            print(f"Offering {offering_id} created but is not available.")
