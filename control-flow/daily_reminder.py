"""
Personal Daily Reminder
"""

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high": 
            if priority == "high" and time_bound == "yes":
                print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
            elif priority == "high" and time_bound =="no":
                print(f"Reminder: {task} is a {priority} priority task that requires  attention sedomly!")
        case "medium":
            if priority == "medium" and time_bound == "yes":
                print(f"Reminder: {task} is a {priority} priority task that requires  attention sedomly!")
            elif priority == "medium" and time_bound =="no":
                print(f"Reminder: {task} is a {priority} priority task that requires  attention later!")
         case "low": 
            if priority == "low" and time_bound == "no":
                print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time")