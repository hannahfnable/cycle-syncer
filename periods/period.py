
class Period:
    def __init__(self, start_date, average_length: int, period_length: int, ovulation_length: int):
        self.start_date = start_date
        self.length = average_length
        self.period_length = period_length
        self.ovulation_length = ovulation_length
        self.end_date = start_date + timedelta(days=average_length)
        self.phases = self.generate_phases()
    
    def generate_phases(self): Phase[]:
        ovulation_day = self.length // 2
        menstruation_length = self.period_length

        menstruation_phase = Phase(PhaseType.MENSTRUATION, self.start_date, menstruation_length)
        follicular_phase = Phase(PhaseType.FOLLICULAR, self.start_date + timedelta(days=menstruation_length), ovulation_day - menstruation_length - 1)
        ovulation_phase = Phase(PhaseType.OVULATION, self.start_date + timedelta(days=ovulation_day) - 1, ovulation_length)
        luteal_phase = Phase(PhaseType.LUTEAL, self.start_date + timedelta(days=ovulation_day + ovulation_length - 1), self.length - ovulation_day - ovulation_length + 1)
        
        return [menstruation_phase, follicular_phase, ovulation_phase, luteal_phase]