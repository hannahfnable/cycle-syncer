
class TimeBlock:
    def __init__(self, day: str, start_hour: int, end_hour: int):
        self.day = day
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.activity = None

    def assign_activity(self, activity: str):
        self.activity = activity

    def clear_activity(self):
        self.activity = None