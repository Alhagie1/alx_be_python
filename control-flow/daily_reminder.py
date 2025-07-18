
# Personal Daily Reminder program

task = input("Describe your task:") # Task Description
priority = input("What is your task priority? (high, medium, low):") # Task priority
time_bound = input("Is the task time-bound (yes/no):")  
match priority:
    case "high":
        priority == "high"
    case "medium":
        priority == "medium"       
    case "low":
        priority == "low"
    case _:
        print("error")
if time_bound == "yes":
     print(f"Reminder: {task} is a high priority task that requires immediate attention")
else:
     print(f"Note: {task} is a low priority task. Consider finishing it in your free time.")



