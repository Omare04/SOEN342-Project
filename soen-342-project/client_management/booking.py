import uuid
from utils.utils import append_csv, read_csv, write_csv, initialize_csv

class Booking:
    
    @staticmethod
    def create_booking(client_id, offering_id):
        """
        Create a booking for a given client and offering ID.
        """
        # Read necessary CSV files
        clients = read_csv('data/clients.csv')
        users = read_csv('data/users.csv')
        offerings = read_csv('data/offerings.csv')

        # Debugging: Print the clients data for validation
        print("Clients data:", clients)

        # Validate client
        client = next((c for c in clients if c.get('client_id FK(user_id)') == str(client_id)), None)
        if not client:
            print(f"Error: Client with ID {client_id} not found in clients.csv.")
            return

        # Cross-check client in `users.csv`
        user = next((u for u in users if u['user_id'] == str(client_id)), None)
        if not user:
            print(f"Error: Client with ID {client_id} not found in users.csv.")
            return

        # Validate offering
        offering = next((o for o in offerings if o.get('offering_id') == offering_id), None)
        if not offering:
            print(f"Error: Offering with ID {offering_id} not found.")
            return

        # Check if the offering is available
        if offering.get('is_available', 'True') == 'False':
            print(f"Error: Offering {offering_id} is not available.")
            return

        # Create the booking
        initialize_csv('data/bookings.csv', ['booking_id', 'client_id FK(user_id)', 'offering_id'])
        bookings = read_csv('data/bookings.csv')
        booking_id = f"B{len(bookings) + 1:03}"

        # Append booking to CSV
        append_csv('data/bookings.csv', {
            'booking_id': booking_id,
            'client_id FK(user_id)': client_id,
            'offering_id': offering_id
        }, fieldnames=['booking_id', 'client_id FK(user_id)', 'offering_id'])

        # Mark offering as unavailable
        for o in offerings:
            if o['offering_id'] == offering_id:
                o['is_available'] = 'False'
                break

        write_csv('data/offerings.csv', offerings, fieldnames=offerings[0].keys())

        print(f"Booking successfully created with ID {booking_id} for Offering {offering_id}.")

    @staticmethod
    def cancel_booking(booking_id):
        bookings = read_csv('data/bookings.csv')
        bookings = [b for b in bookings if b['booking_id'] != booking_id]
        write_csv('data/bookings.csv', bookings, fieldnames=['booking_id', 'offering_id', 'client_id', 'schedule_id', 'is_available'])
        print("Booking canceled successfully.")
