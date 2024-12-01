import random

print("Welcome to Employee Wage Computation Program")

# UC1: Check Employee Attendance
attendance = random.choice([0, 1])
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")

#UC2: Daily Employee Wage
wage_per_hour = 20
full_day_hour = 8
daily_wage = wage_per_hour * full_day_hour
print(f"Daily Employee Wage: {daily_wage}")


#UC3 : Part Time Employee Wage
part_time_hour = 8
part_time_wage = wage_per_hour * part_time_hour
print(f"Part-time Employee Wage: {part_time_wage}")


#UC4 : Solve using Switch Case
def employee_wage(employee_type):
    switcher = {
        1: full_day_hour * wage_per_hour,  # Full-time employee
        2: part_time_hour * wage_per_hour  # Part-time employee
    }
    return switcher.get(employee_type, 0)  # Default for absent

employee_type = random.choice([0, 1, 2])  # 0: Absent, 1: Full-time, 2: Part-time
print(f"Employee Wage: {employee_wage(employee_type)}")

#UC5 : Calculate Wages for a Month
working_days_per_month = 20
monthly_wage = working_days_per_month * daily_wage
print(f"Monthly Employee Wage: {monthly_wage}")

#UC : 6 Calculate Wages Till condition
max_hours_per_month = 100
total_working_days = 0
total_working_hours = 0

while total_working_days < 20 and total_working_hours < max_hours_per_month:
    hours_worked = random.choice([0, 4, 8])  # 0: Absent, 4: Part-time, 8: Full-time
    total_working_hours += hours_worked
    total_working_days += 1

total_wage = total_working_hours * wage_per_hour
print(f"Total Employee Wage for the Month: {total_wage}")


#UC : 7 Refactor code using class method
class EmployeeWageComputation:
    wage_per_hour = 20
    full_day_hour = 8
    part_time_hour = 4

    @classmethod
    def calculate_wage(cls, employee_type):
        if employee_type == 1:  # Full-time
            return cls.full_day_hour * cls.wage_per_hour
        elif employee_type == 2:  # Part-time
            return cls.part_time_hour * cls.wage_per_hour
        else:
            return 0  # Absent

employee_type = random.choice([0, 1, 2])  # 0: Absent, 1: Full-time, 2: Part-time
wage = EmployeeWageComputation.calculate_wage(employee_type)
print(f"Employee Wage: {wage}")
