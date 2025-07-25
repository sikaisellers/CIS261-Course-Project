#Sikai Sellers CIS261 Course Project Phase 1
#Input Instructions
def get_input(prompt, is_float=False):
    while True:
        value = input(prompt).strip()
        if value == "End" or (not is_float and value):
            return value
        try:
            num = float(value)
            if num >= 0:
                return num
        except:
            pass
        print("Please input a valid entry.")

#Payroll Calculation
def calculate_pay(hours, rate, tax_rate):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net

#Payroll Details
def display_employee(name, hours, rate, gross, tax_rate, tax, net):
    print(f"\nEmployee Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Income Tax Rate: {tax_rate:.2%}")
    print(f"Income Tax: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")

#All Employees Details
def display_summary(emp_count, total_hours, total_gross, total_tax, total_net):
    print("\n--- Payroll Summary ---")
    print(f"Total Employees: {emp_count}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Income Taxes: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net:.2f}")

#Main Payroll
def run_payroll():
    emp_count = total_hours = total_gross = total_tax = total_net = 0
    while True:
        name = get_input("Enter employee name (or 'End' to finish): ")
        if name == "End":
            break
        hours = get_input("Enter total hours worked: ", True)
        rate = get_input("Enter hourly rate: ", True)
        tax_rate = get_input("Enter income tax rate (as a decimal): ", True)
        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        display_employee(name, hours, rate, gross, tax_rate, tax, net)
        emp_count += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net
    display_summary(emp_count, total_hours, total_gross, total_tax, total_net)

run_payroll()

