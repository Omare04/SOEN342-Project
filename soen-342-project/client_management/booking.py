# client_management/booking.py
from utils.utils import append_csv, read_csv, write_csv, initialize_csv

class Booking:
    @staticmethod
# client_management/booking.py

    @staticmethod
    def create_booking(client_name, offering_id):
        # Load clients and guardians to verify relationships
        clients = read_csv('data/clients.csv')
        guardians = read_csv('data/guardian.csv')
        
        # Verify the client exists
        client = next((c for c in clients if c['name'] == client_name), None)
        if not client:
            print("Error: Client not registered.")
            return

        # If the client is underage, verify they have a guardian
        if int(client['age']) < 18:
            guardian = next((g for g in guardians if g['minor_name'] == client_name), None)
            if not guardian:
                print("Error: Underage client must have a registered guardian.")
                return

        # Proceed with booking
        booking = {'client_name': client_name, 'offering_id': offering_id}
        initialize_csv('data/bookings.csv', ['client_name', 'offering_id'])
        append_csv('data/bookings.csv', booking, fieldnames=['client_name', 'offering_id'])
        print("Booking created successfully.")

            
    def cancel_booking(client_name, offering_id):
        bookings = read_csv('data/bookings.csv')
        bookings = [b for b in bookings if not (b['client_name'] == client_name and b['offering_id'] == offering_id)]
        write_csv('data/bookings.csv', bookings, fieldnames=['client_name', 'offering_id'])
        print("Booking canceled successfully.")
