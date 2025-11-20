from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    new_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {new_current_date}")
    return current_date


# Calculate the future time with plus date 
def calculate_future_date(): 
    requested_time = int(input(f"Enter the number of days to add to the current date:  "))
    future_date = display_current_datetime() + timedelta(requested_time)
    new_future_date = future_date.strftime("%Y-%m-%d %H-%M-%S")
    return print(f"Future date: {new_future_date}")


calculate_future_date()