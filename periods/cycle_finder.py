class Cycle_Finder:
    def __init__(self, last_period: datetime, previous_period: datetime, estimated_length: number, period_length: number):
        self.estimated_length = estimated_length
        self.period_length = period_length
        self.cycle_length = get_average_cycle_length()
        self.Periods = []Period(last_period_days, previous_period)

    def new_period(self, new_period_date: datetime):
        self.Periods[-1].end_date = new_period_date
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

        return total_length / len(self.Periods) + 1 
    

 