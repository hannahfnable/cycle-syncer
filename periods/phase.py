
from datetime import datetime, timedelta

class Phase:
    def __init__(self, name: str, day: datetime, phase_length: int):
        self.name = name
        self.start_date = day
        self.end_date = day + timedelta(days=phase_length)
        self.length = phase_length
