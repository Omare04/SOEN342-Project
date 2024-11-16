from utils.utils import append_csv, initialize_csv, read_csv, write_csv

class User:
    def __init__(self, user_id, name, phone, email):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def register_user(user_id, name, phone, email, user_type):
        """
        Register a user in the shared `users.csv` file.
        """
        initialize_csv('data/users.csv', ['user_id', 'name', 'phone', 'email', 'user_type'])
        append_csv('data/users.csv', {
            'user_id': user_id,
            'name': name,
            'phone': phone,
            'email': email,
            'user_type': user_type
        }, fieldnames=['user_id', 'name', 'phone', 'email', 'user_type'])
        print(f"{user_type.capitalize()} {name} registered successfully with ID {user_id}.")

    @staticmethod
    def view_all_users():
        """
        Display all users in the `users.csv` file.
        """
        users = read_csv('data/users.csv')
        if not users:
            print("No users found.")
            return
        print("\nAll Registered Users:")
        print(f"{'ID':<10}{'Name':<20}{'Phone':<15}{'Email':<30}{'User Type':<15}")
        print("=" * 90)
        for user in users:
            print(f"{user['user_id']:<10}{user['name']:<20}{user['phone']:<15}{user['email']:<30}{user['user_type']:<15}")
        print("=" * 90)
