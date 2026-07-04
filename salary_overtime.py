# Program to calculate overtime hours and overtime pay at 1.5x the hourly rate
standard_working_hours = 8
hourly_rate = 1.5

# Take input from user for standard salary and worked hour
standard_salary = float(input("Enter standard salary: "))
worked_hours = float(input("Enter total hours worked: "))

# Calculate overtime hours by subtracting standard hours from total hours worked
overtime_hours = worked_hours - standard_working_hours 

# Calculating overtime pay and total salary
overtime_pay = standard_salary * hourly_rate * overtime_hours / standard_working_hours
total_salary = standard_salary + overtime_pay

# printing salary
if worked_hours > standard_working_hours:
    print(f"Overtime hours: {overtime_hours}")
    print(f"Total salary including overtime pay: {total_salary:.2f}")
else:
    print(f"No overtime hours. salary: {standard_salary:.2f}")
