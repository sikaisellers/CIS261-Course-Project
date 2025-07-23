# Sikai Sellers CIS261 Course Project

def input_employee_data():
    name = input("Enter employee name (or 'End' to finish): ")
    if name.lower() == "end":
        return None
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("enter income tax rate (as a decimal, e.g. 0.2 for 20%): "))
    return {
        "name": name,
        "hours_worked": hours_worked,
        "hourly_rate": hourly_rate,
        "tax_rate": tax_rate
    }