import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date


# Calculate the future time with plus date 
def calculate_future_date(): 
    requested_time = int(input("Enter the number of days: "))
    future_date = display_current_datetime() + datetime.timedelta(requested_time)
    return print(future_date)


calculate_future_date()