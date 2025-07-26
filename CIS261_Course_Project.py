# === Payroll Calculator - Proof of Concept ===

# --- Input Functions ---
def get_employee_name():
    # Prompts user for employee name or 'End' to finish
    return input("Enter employee name (or 'End' to finish): ")

def get_total_hours():
    # Gets total hours worked as a float
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    # Gets hourly pay rate as a float
    return float(input("Enter hourly rate: $"))

def get_tax_rate():
    # Gets income tax rate in decimal form (e.g., 0.2 for 20%)
    return float(input("Enter income tax rate (e.g., 0.2 for 20%): "))


# --- Calculation Logic ---
def calculate_pay(hours, rate, tax_rate):
    # Calculates gross pay, tax amount, and net pay
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay


# --- Display Individual Employee Data ---
def display_employee_info(name, hours, rate, tax_rate, gross_pay, income_tax, net_pay):
    # Outputs formatted payroll info for one employee
    print("\nEmployee Information")
    print(f"Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")
    print("-" * 40)


# --- Display Totals for All Employees ---
def display_totals(employee_count, total_hours, total_gross, total_tax, total_net):
    # Outputs cumulative payroll summary
    print("\nSummary of All Employees")
    print(f"Total Employees: {employee_count}")
    print(f"Total Hours Worked: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Income Taxes: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")


# === Main Execution Block ===

# --- Totals Initialization ---
employee_count = 0
total_hours = 0
total_gross = 0
total_tax = 0
total_net = 0

# --- Input Loop ---
while True:
    name = get_employee_name()
    if name.lower() == "end":
        # Terminates loop if sentinel value is entered
        break
    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
    display_employee_info(name, hours, rate, tax_rate, gross_pay, income_tax, net_pay)

    # Aggregate totals for final summary
    employee_count += 1
    total_hours += hours
    total_gross += gross_pay
    total_tax += income_tax
    total_net += net_pay

# --- Final Summary Output ---
display_totals(employee_count, total_hours, total_gross, total_tax, total_net)
