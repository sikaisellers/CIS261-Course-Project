# Sikai Sellers CIS261 Phase 3

import re  # For date validation

# Input Functions
def get_date_range():
    # Prompts for date range in mm/dd/yyyy format
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date

def get_employee_name():
    return input("Enter employee name (or 'End' to finish): ")

def get_total_hours():
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: $"))

def get_tax_rate():
    return float(input("Enter income tax rate (e.g., 0.2 for 20%): "))

# Pay Calculations
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Individual Employees
def display_employee_info(emp_data):
    print("\nEmployee Information")
    print(f"Date Range: {emp_data['from_date']} to {emp_data['to_date']}")
    print(f"Name: {emp_data['name']}")
    print(f"Hours Worked: {emp_data['hours']:.2f}")
    print(f"Hourly Rate: ${emp_data['rate']:.2f}")
    print(f"Gross Pay: ${emp_data['gross_pay']:.2f}")
    print(f"Income Tax Rate: {emp_data['tax_rate']:.2%}")
    print(f"Income Tax: ${emp_data['income_tax']:.2f}")
    print(f"Net Pay: ${emp_data['net_pay']:.2f}")
    print("-" * 40)

# Totals
def display_totals(totals):
    print("\nSummary of All Employees")
    print(f"Total Employees: {totals['employee_count']}")
    print(f"Total Hours Worked: {totals['total_hours']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross']:.2f}")
    print(f"Total Income Taxes: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net']:.2f}")

# Save record to file
def write_record_to_file(emp):
    with open("employee_data.txt", "a") as file:
        file.write(f"{emp['from_date']}|{emp['to_date']}|{emp['name']}|{emp['hours']}|{emp['rate']}|{emp['tax_rate']}\n")

# Validate date format
def is_valid_date(date_str):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", date_str)

# Report Generator
def generate_report():
    date_input = input("\nEnter FROM date for report (mm/dd/yyyy) or 'all': ").strip().lower()
    while date_input != "all" and not is_valid_date(date_input):
        print("Invalid date format. Please use mm/dd/yyyy.")
        date_input = input("Enter FROM date for report (mm/dd/yyyy) or 'all': ").strip().lower()

    print("\nReport Results:")

    totals = {
        "employee_count": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    with open("employee_data.txt", "r") as file:
        for line in file:
            from_date, to_date, name, hours, rate, tax_rate = line.strip().split("|")

            if date_input == "all" or from_date == date_input:
                hours = float(hours)
                rate = float(rate)
                tax_rate = float(tax_rate)
                gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

                emp_data = {
                    "from_date": from_date,
                    "to_date": to_date,
                    "name": name,
                    "hours": hours,
                    "rate": rate,
                    "tax_rate": tax_rate,
                    "gross_pay": gross_pay,
                    "income_tax": income_tax,
                    "net_pay": net_pay
                }

                display_employee_info(emp_data)

                totals["employee_count"] += 1
                totals["total_hours"] += hours
                totals["total_gross"] += gross_pay
                totals["total_tax"] += income_tax
                totals["total_net"] += net_pay

    display_totals(totals)

# Main Program
employee_records = []

# Input Loop
while True:
    name = get_employee_name()
    if name.lower() == "end":
        break
    from_date, to_date = get_date_range()
    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    emp = {
        "name": name,
        "from_date": from_date,
        "to_date": to_date,
        "hours": hours,
        "rate": rate,
        "tax_rate": tax_rate
    }

    employee_records.append(emp)
    write_record_to_file(emp)  # Save to file

# Generate Report
generate_report()
