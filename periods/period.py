
from datetime import datetime, timedelta

from enums.phase_type import PhaseType
from periods.phase import Phase


class Period:
    def __init__(self, start_date: datetime, end_date: datetime, average_length: int, period_length: int, ovulation_length: int):
        self.period_id = id(self)
        self.start_date = start_date
        if end_date:
            self.end_date = end_date
            self.length = (self.end_date - self.start_date).days
        else:
            self.end_date = start_date + timedelta(days=average_length)
            self.length = average_length
        self.phases = self.estimate_phases(period_length, ovulation_length)
    
    def update_actual_end_date(self, actual_end_date: datetime):
        self.end_date = actual_end_date
        self.length = (self.end_date - self.start_date).days
    
    def estimate_phases(self, period_length, ovulation_length) -> list[Phase]:
        ovulation_day = self.length // 2
        menstruation_length = self.period_length

        menstruation_phase = Phase(PhaseType.MENSTRUATION, self.start_date, menstruation_length)
        follicular_phase = Phase(PhaseType.FOLLICULAR, self.start_date + timedelta(days=menstruation_length), ovulation_day - menstruation_length - 1)
        ovulation_phase = Phase(PhaseType.OVULATION, self.start_date + timedelta(days=ovulation_day) - 1, ovulation_length)
        luteal_phase = Phase(PhaseType.LUTEAL, self.start_date + timedelta(days=ovulation_day + ovulation_length - 1), self.length - ovulation_day - ovulation_length + 1)
        
        return [menstruation_phase, follicular_phase, ovulation_phase, luteal_phase]