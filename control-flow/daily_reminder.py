
# Personal Daily Reminder program

Task = input("What is your task? :") # Task Description

Priority = input("What is the priority level of your task (high, medium, low): ").lower() # Task priority

Time_bound = input("Is your task time-boun?  (yes/no) :").lower() 

priority_description = ""
priority_is_valid = True

match Priority:
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
     if Time_bound  == "yes":
         print(f"Reminder: {Task} is {priority_description} task that requires immediate attention")
     elif Time_bound == "no":
         print(f"Note: {Task} is a {priority_description}. Consider finishing it in your free time.")
     else:
         print("Entered an invalid time bound just answer (yes or no) ")





