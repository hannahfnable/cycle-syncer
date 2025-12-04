

class User:
    def __init__(self, last_period: datetime, previous_period: datetime, estimated_length: number, period_length: number):
        self.cycle_finder = Cycles_Finder(last_period, previous_period, estimated_length, period_length)
        self.estimated_next_cycle = self.cycle_finder.create_next_cycle()
