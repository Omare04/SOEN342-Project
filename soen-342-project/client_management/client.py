from utils.utils import append_csv, initialize_csv, read_csv, write_csv

class Client:
    
    def __init__(self, name, phone, email, age, guardian_id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.guardian_id = guardian_id
        
    
    @staticmethod
    def register(name, phone, email, age, guardian_id=None):
        # Check if the client is underage and has a guardian
        if int(age) < 18 and not guardian_id:
            print("Error: Underage clients must have a guardian.")
            return

        # Initialize `clients.csv` with headers if it doesn't exist
        initialize_csv('data/clients.csv', ['client_id', 'name', 'phone', 'email', 'age', 'guardian_id'])
        clients = read_csv('data/clients.csv')
        client_id = len(clients) + 1  # Auto-incremented client ID

        # Append client data to `clients.csv`
        append_csv('data/clients.csv', {
            'client_id': client_id,
            'name': name,
            'phone': phone,
            'email': email,
            'age': age,
            'guardian_id': guardian_id
        }, fieldnames=['client_id', 'name', 'phone', 'email', 'age', 'guardian_id'])
        print(f"Client {name} registered successfully with ID {client_id}.")

        # If the client is underage, add them to `guardians.csv`
        if int(age) < 18:
            initialize_csv('data/guardians.csv', ['guardian_id', 'guardian_name', 'minor_name', 'minor_age'])
            guardians = read_csv('data/guardians.csv')
            guardian = next((g for g in guardians if int(g['guardian_id']) == int(guardian_id)), None)

            if guardian:
                append_csv('data/guardians.csv', {
                    'guardian_id': guardian_id,
                    'guardian_name': guardian['guardian_name'],
                    'minor_name': name,
                    'minor_age': age  # Correctly add the age of the minor
                }, fieldnames=['guardian_id', 'guardian_name', 'minor_name', 'minor_age'])
                print(f"Minor {name} (age {age}) added to guardian {guardian['guardian_name']} in guardians.csv.")
            else:
                print("Error: Guardian ID not found. Unable to link minor to guardian.")

    @staticmethod
    def register_guardian(guardian_name, minor_name, minor_age):
        # Ensure the minor is underage
        if int(minor_age) >= 18:
            print("Error: Guardians are only required for clients under 18.")
            return

        # Initialize `guardians.csv` and append guardian data
        initialize_csv('data/guardians.csv', ['guardian_id', 'guardian_name', 'minor_name', 'minor_age'])
        append_csv('data/guardians.csv', {
            'guardian_name': guardian_name,
            'minor_name': minor_name,
            'minor_age': minor_age
        }, fieldnames=['guardian_id', 'guardian_name', 'minor_name', 'minor_age'])
        print("Guardian registered successfully.")

    
    @staticmethod
    def view_client_details(client_id):
        """
        Display details of a specific client by their ID.
        """
        # Read both `clients.csv` and `users.csv`
        clients = read_csv('data/clients.csv')
        users = read_csv('data/users.csv')

        # Validate and locate the client in `clients.csv`
        client = next((c for c in clients if c.get('client_id FK(user_id)') == str(client_id)), None)
        if not client:
            print(f"Error: Client with ID {client_id} not found in clients.csv.")
            return

        # Validate and locate the user's details in `users.csv`
        user = next((u for u in users if u['user_id'] == str(client_id)), None)
        if not user:
            print(f"Error: User with ID {client_id} not found in users.csv.")
            return

        # Display the combined client details
        print("\nClient Details:")
        print(f"ID: {client['client_id FK(user_id)']}")
        print(f"Name: {user['name']}")
        print(f"Phone: {user['phone']}")
        print(f"Email: {user['email']}")
        print(f"Age: {client['age']}")
        print(f"Guardian ID: {client.get('guardian_id FK(guardian_id)', 'N/A')}")

    @staticmethod
    def view_available_offerings():
        """
        View all available offerings for the client.
        """
        offerings = read_csv('data/offerings.csv')
        locations = read_csv('data/locations.csv')
        schedules = read_csv('data/schedules.csv')

        if not offerings:
            print("No offerings found.")
            return

        # Print the table header
        print("\nAvailable Offerings:")
        print(f"{'Offering ID':<15}{'Lesson Type':<20}{'Location':<25}{'Schedule':<25}")
        print("=" * 85)

        # Display only available offerings
        for offering in offerings:
            if offering['is_available'].lower() == 'true':
                location = next((loc for loc in locations if loc['location_id'] == offering['location_id']), None)
                schedule = next((sch for sch in schedules if sch['schedule_id'] == offering['schedule_id']), None)

                location_name = location['name'] if location else "Unknown Location"
                schedule_info = f"{schedule['start_date']} to {schedule['end_date']} ({schedule['day']})" if schedule else "Unknown Schedule"

                print(f"{offering['offering_id']:<15}{offering['lesson_type']:<20}{location_name:<25}{schedule_info:<25}")
        print("=" * 85)

    @staticmethod
    def view_client_bookings(client_id):
        """
        View bookings associated with a specific client ID.
        """
        bookings = read_csv('data/bookings.csv')
        offerings = read_csv('data/offerings.csv')
        schedules = read_csv('data/schedules.csv')

        # Filter bookings for the given client ID
        client_bookings = [b for b in bookings if b['client_id'] == str(client_id)]

        if not client_bookings:
            print(f"No bookings found for Client ID: {client_id}")
            return

        # Display the bookings
        print(f"\nBookings for Client ID: {client_id}")
        print(f"{'Booking ID':<15}{'Offering ID':<15}{'Schedule':<25}{'Available':<10}")
        print("=" * 70)

        for booking in client_bookings:
            schedule = next((s for s in schedules if s['schedule_id'] == booking['schedule_id']), None)
            schedule_info = f"{schedule['start_date']} to {schedule['end_date']} ({schedule['day']})" if schedule else "Unknown Schedule"

            print(
                f"{booking['booking_id']:<15}{booking['offering_id']:<15}{schedule_info:<25}{booking['is_available']:<10}"
            )
