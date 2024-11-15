from datetime import date, time

class Schedule:
    def __init__(self, start_date, end_date, start_time, end_time, day):
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def is_available(self):
        pass
