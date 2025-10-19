import csv
import random
from datetime import datetime, timedelta

# define sample data
departments = ['HR', 'Finance', 'IT', 'Marketing', 'Operations', 'Admin']
genders = ['Male', 'Female']

# generate random employee data
def create_employee_data(num_records=1000):
    data = []
    base_date = datetime(2010, 1, 1)
    for emp_id in range(1, num_records + 1):
        name = f"Employee_{emp_id}"
        dept = random.choice(departments)
        salary = random.randint(30000, 120000)
        gender = random.choice(genders)
        join_date = base_date + timedelta(days=random.randint(0, 5500))
        dept_id = departments.index(dept) + 1
        data.append([emp_id, name, dept_id, salary, gender, join_date.strftime('%Y-%m-%d')])
    return data

# write data to CSV
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["EmpID", "Name", "DeptID", "Salary", "Gender", "JoinDate"])
    writer.writerows(create_employee_data(5000))  # modifies number of rows

print("employees.csv file created successfully!")
