# Finance Calculator Program

# Monthly Income
monthly_income = int(input("Enter your monthly income:"))
print(f"your monthly income is: {monthly_income}")
# Monthly Expenses
monthly_expenses = int(input("Enter your monthly expenses:"))
print(f"Your Monthly expenses is: {monthly_expenses}")

# Formula for calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected Annnual Savings

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Your Projected Annual Savings is : {projected_annual_savings}")
