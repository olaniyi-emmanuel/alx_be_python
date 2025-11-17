"""
Personal Daily Reminder
"""

def daily_reminder():
    task = input("Enter your task: ")
    priority_level = input("Priority (high/medium/low): ")
    time_sensitive = input("Is it time-bound? (yes/no)")

    match priority_level:
        case "high": 
            if priority_level == "high" and time_sensitive == "yes":
                print(f"Reminder: {task} is a {priority_level} priority task that requires immediate attention today!")
            elif priority_level == "high" and time_sensitive =="no":
                print(f"Reminder: {task} is a {priority_level} priority task that requires  attention sedomly!")
        case "medium":
            if priority_level == "medium" and time_sensitive == "yes":
                print(f"Reminder: {task} is a {priority_level} priority task that requires  attention sedomly!")
            elif priority_level == "medium" and time_sensitive =="no":
                print(f"Reminder: {task} is a {priority_level} priority task that requires  attention later!")
         case "low": 
            if priority_level == "low" and time_sensitive == "no":
                print(f"Reminder: {task} is a {priority_level} priority task. Consider completing it when you have free time")