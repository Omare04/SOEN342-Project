from User import User
from utils.utils import read_csv, initialize_csv, append_csv

class Guardian(User):
    def __init__(self, user_id, name, phone, email, assigned_client_id=None):
        super().__init__(user_id, name, phone, email)  # Inherit common attributes
        self.assigned_client_id = assigned_client_id  # One-to-one relationship with a client

    @staticmethod
    def register(name, phone, email, client_id):
        """
        Register a guardian and assign them to a specific client (underage).
        """
        # Validate client existence and age
        clients = read_csv('data/clients.csv')
        client = next((c for c in clients if int(c['client_id']) == int(client_id)), None)
        if not client:
            print("Error: Client not found.")
            return
        if int(client['age']) >= 18:
            print("Error: Guardians can only be assigned to clients under 18.")
            return

        # Generate unique guardian ID
        guardians = read_csv('data/guardians.csv')
        guardian_id = len(guardians) + 1  # Auto-incremented ID

        # Register in `users.csv` as a `Guardian`
        User.register_user(guardian_id, name, phone, email, "Guardian")

        # Initialize `guardians.csv` if it doesn't exist
        initialize_csv('data/guardians.csv', ['guardian_id', 'assigned_client_id'])

        # Append guardian-specific data to `guardians.csv`
        append_csv('data/guardians.csv', {
            'guardian_id': guardian_id,
            'assigned_client_id': client_id
        }, fieldnames=['guardian_id', 'assigned_client_id'])
        print(f"Guardian {name} registered successfully with ID {guardian_id} and assigned to client {client_id}.")

    @staticmethod
    def view_my_details(guardian_id):
        """
        View the details of the logged-in guardian, including their assigned client.
        """
        # Fetch guardian details
        guardians = read_csv('data/guardians.csv')
        guardian = next((g for g in guardians if int(g['guardian_id']) == int(guardian_id)), None)
        if not guardian:
            print("Error: Guardian not found.")
            return

        # Fetch corresponding user details
        users = read_csv('data/users.csv')
        user = next((u for u in users if int(u['user_id']) == int(guardian_id) and u['user_type'] == "Guardian"), None)
        if not user:
            print("Error: Guardian user details not found.")
            return

        # Fetch client details
        clients = read_csv('data/clients.csv')
        client = next((c for c in clients if int(c['client_id']) == int(guardian['assigned_client_id'])), None)

        # Display details
        print("\nYour Guardian Details:")
        print(f"Guardian ID: {guardian_id}")
        print(f"Name: {user['name']}")
        print(f"Phone: {user['phone']}")
        print(f"Email: {user['email']}")
        if client:
            print(f"Assigned Client: {client['name']} (Client ID: {client['client_id']}, Age: {client['age']})")
        else:
            print("Assigned Client: None")
