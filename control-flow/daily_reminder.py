"""
Personal Daily Reminder
"""

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

        # Use match/case for priority, combined with a guard (if) for time-bound status.
    match priority:
        
        # High Priority Cases
        case "high" if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires IMMEDIATE attention today!")
        
        case "high": # Catches "high" priority when time_bound is "no" or otherwise
            print(f"Reminder: '{task}' is a {priority} priority task. Schedule for the next available slot.")
        
        # Medium Priority Cases
        case "medium" if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task. Aim to complete by the end of the day.")
            
        case "medium": # Catches "medium" priority when time_bound is "no" or otherwise
            print(f"Reminder: '{task}' is a {priority} priority task. Handle after high priority tasks.")

        # Low Priority Cases
        case "low" if time_bound == "yes":
            print(f"Reminder: '{task}' is a time-bound, {priority} priority task. Handle it today if possible.")
        
        case "low": # Catches "low" priority when time_bound is "no" or otherwise
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
            
        # Default Case for invalid input
        case _:
            print("Invalid priority entered. Please check your input (must be high, medium, or low).")