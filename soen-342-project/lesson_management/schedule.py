class Schedule:
    def __init__(self, schedule_id, start_date, end_date, start_time, end_time, day):
        self.schedule_id = schedule_id
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.day = day

    def is_available(self, date_to_check):
        return self.start_date <= date_to_check <= self.end_date
