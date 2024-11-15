class Room:
    def __init__(self, room_number, is_available=True):
        self.room_number = room_number
        self.is_available = is_available
        self.offerings = []
