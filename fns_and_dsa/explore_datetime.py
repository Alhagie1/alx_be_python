
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
    number_of_days = int(input("Enter number of days to add to the current date: "))
    def calculate_future_date(current_date, days_to_add):
       future_date = current_date + datetime.timedelta(days = days_to_add)
       return future_date  
    final_future_date = calculate_future_date(current_date, number_of_days)
    print(f"Future date: {final_future_date.strftime("%Y-%m-%d %H:%M:%S")}")
display_current_datetime()
    