import re

# --- Login Class ---
class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

# --- User Management ---
def load_users(filename="user_login.txt"):
    user_ids, credentials = [], []
    try:
        with open(filename, "r") as file:
            for line in file:
                uid, pwd, auth = line.strip().split("|")
                user_ids.append(uid)
                credentials.append((uid, pwd, auth))
    except FileNotFoundError:
        pass
    return user_ids, credentials

def add_users():
    user_ids, _ = load_users()
    with open("user_login.txt", "a") as file:
        while True:
            user_id = input("Enter new User ID (or 'End' to finish): ").strip()
            if user_id.lower() == "end":
                break
            if user_id in user_ids:
                print("User ID already exists.")
                continue
            password = input("Enter Password: ").strip()
            auth = input("Enter Authorization Code ('admin' or 'user'): ").strip().lower()
            if auth not in ["admin", "user"]:
                print("Invalid authorization code.")
                continue
            file.write(f"{user_id}|{password}|{auth}\n")
            user_ids.append(user_id)
            print("User added successfully.")

def login():
    _, credentials = load_users()
    user_id = input("Login - Enter User ID: ").strip()
    password = input("Enter Password: ").strip()
    for uid, pwd, auth in credentials:
        if uid == user_id:
            if pwd == password:
                print("Login successful.\n")
                return Login(uid, pwd, auth)
            else:
                print("Incorrect password.")
                exit()
    print("User ID not found.")
    exit()

# --- Payroll Functions ---
def get_date_range():
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

def calculate_pay(hours, rate, tax_rate):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net

def display_employee_info(emp):
    print("\nEmployee Information")
    print(f"Date Range: {emp['from_date']} to {emp['to_date']}")
    print(f"Name: {emp['name']}")
    print(f"Hours Worked: {emp['hours']:.2f}")
    print(f"Hourly Rate: ${emp['rate']:.2f}")
    print(f"Gross Pay: ${emp['gross_pay']:.2f}")
    print(f"Income Tax Rate: {emp['tax_rate']:.2%}")
    print(f"Income Tax: ${emp['income_tax']:.2f}")
    print(f"Net Pay: ${emp['net_pay']:.2f}")
    print("-" * 40)

def display_totals(totals):
    print("\nSummary of All Employees")
    print(f"Total Employees: {totals['employee_count']}")
    print(f"Total Hours Worked: {totals['total_hours']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross']:.2f}")
    print(f"Total Income Taxes: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net']:.2f}")

def write_record_to_file(emp):
    with open("employee_data.txt", "a") as file:
        file.write(f"{emp['from_date']}|{emp['to_date']}|{emp['name']}|{emp['hours']}|{emp['rate']}|{emp['tax_rate']}\n")

def is_valid_date(date_str):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", date_str)

def generate_report(login_obj):
    date_input = input("\nEnter FROM date for report (mm/dd/yyyy) or 'all': ").strip().lower()
    while date_input != "all" and not is_valid_date(date_input):
        print("Invalid date format.")
        date_input = input("Enter FROM date for report (mm/dd/yyyy) or 'all': ").strip().lower()

    print("\nReport Results:")
    print(f"User ID: {login_obj.user_id}")
    print(f"Password: {login_obj.password}")
    print(f"Authorization: {login_obj.authorization}")
    print("-" * 40)

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
                gross, tax, net = calculate_pay(hours, rate, tax_rate)

                emp_data = {
                    "from_date": from_date,
                    "to_date": to_date,
                    "name": name,
                    "hours": hours,
                    "rate": rate,
                    "tax_rate": tax_rate,
                    "gross_pay": gross,
                    "income_tax": tax,
                    "net_pay": net
                }

                display_employee_info(emp_data)

                totals["employee_count"] += 1
                totals["total_hours"] += hours
                totals["total_gross"] += gross
                totals["total_tax"] += tax
                totals["total_net"] += net

    display_totals(totals)

# --- Main Program ---
add_users()  # Optional: run once to add users
login_obj = login()

if login_obj.authorization == "admin":
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

        write_record_to_file(emp)

generate_report(login_obj)

