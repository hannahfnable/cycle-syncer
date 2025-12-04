
class Timetable:
    def __init__():
        self.timeblocks = generate_timeblocks()

    def generate_timeblocks():
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        timeblocks = []
        for day in days:
            for hour in range(6, 21, 1): # Create 1-hour blocks from 6 AM to 9 PM
                timeblock = TimeBlock(day, hour, hour + 1)
                timeblocks.append(timeblock)
        return timeblocks
    
    def set_activities(self, activities: list):
        for i, activity in enumerate(activities):
            if i < len(self.timeblocks):
                self.timeblocks[i].assign_activity(activity)


        
        