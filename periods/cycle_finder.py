from operator import attrgetter 
from datetime import datetime, timedelta

from periods.period import Period
class Cycle_Finder:
    def __init__(self, last_period: datetime, previous_period: datetime, estimated_length: int, period_length: int):
        self.estimated_length = estimated_length
        self.period_length = period_length
        self.Periods = self.initialize_periods(last_period, previous_period)
        self.get_average_cycle_length()
        self.get_ovulation_length()
        self.next_cycle = self.create_next_cycle()


    def initialize_periods(self, last_period: datetime, previous_period: datetime):
        periods = []
        periods.append(Period(previous_period, self.cycle_length, self.period_length, 6))
        periods.append(Period(last_period, self.cycle_length, self.period_length, 6))
        return periods

    def add_new_period(self, new_period_date: datetime):
        self.Periods[-1].update_actual_end_date(new_period_date)
        self.Periods.append(Period(new_period_date, None))
        self.get_average_cycle_length()

    def remove_period_date(self, period_date: datetime):
        for period in self.Periods:
            if period.end_date == period_date:
                period.end_date = None
                break
            
    def get_average_cycle_length(self):
        total_length = self.estimated_length
        for period in self.Periods:
            total_length += period.length
        
        self.cycle_length = total_length / len(self.Periods) + 1 
        return self.cycle_length
    
    def get_ovulation_length(self):
        min_length = min(self.Periods,key=attrgetter('length'))
        max_length = max(self.Periods,key=attrgetter('length'))
        start_day = min_length - 18
        end_day = max_length - 11
        self.ovulation_length = end_day - start_day

    def create_next_cycle(self):
        if not self.Periods:
            return None
        last_period = self.Periods[-1]
        next_start_date = last_period.start_date + timedelta(days=self.cycle_length)
        self.next_cycle = Period(next_start_date, self.cycle_length, self.period_length, ovulation_length=3)
        return self.next_cycle
    

 