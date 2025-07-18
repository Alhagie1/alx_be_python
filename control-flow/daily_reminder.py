
# Personal Daily Reminder program

task = input("Enter your task :").strip()
priority = input("Priority(high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound ?(yes/no) :").strip().lower()
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
        print("Error: Choose high , low or medium")
        priority_is_valid = False
if priority_is_valid:
     if time_bound  == "yes":
         print(f"Reminder: {task} is {priority_description} task that requires immediate attention")
     elif time_bound == "no":
         print(f"Note: {task} is a {priority_description}. Consider finishing it in your free time.")
     else:
         print(f"Entered an invalid time bound just answer (yes or no) ")





