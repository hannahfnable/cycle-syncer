
class Phase(self, name: PhaseType, day: datetime, phase_length: int):
    def __init__(self, name: PhaseType, day: datetime, phase_length: int):
        self.name = name
        self.start_date = day
        self.end_date = day + timedelta(days=phase_length)
        self.length = phase_length
