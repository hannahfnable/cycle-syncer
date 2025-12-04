
print("Welcome to the Cycle Syncer!")
from periods.cycle_finder import Cycle_Finder
from user.user import User
from datetime import datetime
if __name__ == "__main__":
    last_period = Input("Enter the date of your last period (YYYY-MM-DD): ")
    last_period = datetime(last_period)
    previous_period = Input("Enter the date of your previous period (YYYY-MM-DD): ")
    previous_period = datetime(previous_period)
    estimated_length = Input("How long is your normal cycle length (in days)?: ")
    period_length = Input("How long does your period usually last (in days)?: ")

print("Calculating your cycles...")   
    user = User(last_period, previous_period, estimated_length, period_length)
    print(f"Your average cycle is {user.cycle_finder.cycle_length} days")