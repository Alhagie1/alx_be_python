
# Personal Daily Reminder program

task = input("Describe your task:") # Task Description

priority = input("What is your task priority? (high, medium, low):").lower() # Task priority

time_bound = input("Is the task time-bound (yes/no):").lower() 

priority_description = ""
priority_is_valid = True

match priority:
    case "high":
        priority_description = "a high priority task"
    case "medium":
        priority_description = "medium priority task"       
    case "low":
        priority_description = "low priority task"
    case _:
        print("error")
        priority_is_valid = False

if priority_is_valid:
     if time_bound  == "yes":
         print(f"Reminder: {task} is {priority_description} task that requires immediate attention")
     elif time_bound == "no":
         print(f"Note: {task} is a {priority_description}. Consider finishing it in your free time.")
     else:
         print("Entere an invalid time bound just answer yes or no")
else:
  print(f"{priority_is_valid} is False")




