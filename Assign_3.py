employees = []

total_gross = 0
total_deductions = 0
total_net = 0

print("========== PAYROLLPRO ==========")

while True:

    n = int(input("Enter number of employees (minimum 3): "))

    if n >= 3:
        break
    else:
        print("Please enter at least 3 employees.")


for i in range(n):

    print("\nEnter Employee", i + 1, "Details")

    name = input("Enter employee name: ")

    emp_id = input("Enter employee ID: ")

    salary = float(input("Enter basic salary: "))

    while salary < 0:

        print("Negative salary is not allowed!")

        salary = float(input("Enter salary again: "))

    hra = salary * 0.20

    travel = salary * 0.05

    gross = salary + hra + travel

    pf = salary * 0.08

    tax = gross * 0.05

    deduction = pf + tax

    net = gross - deduction

    employee = [name, emp_id, salary, hra, travel,
                gross, pf, tax, deduction, net]

    employees.append(employee)

    total_gross += gross

    total_deductions += deduction

    total_net += net

for emp in employees:

    print("\n================================")
    print("   PAYROLLPRO - SALARY BREAKDOWN")
    print("================================")

    print("Employee Name:", emp[0])

    print("Employee ID:", emp[1])

    print("Basic Salary: ₹{:.2f}".format(emp[2]))

    print("HRA (20%): ₹{:.2f}".format(emp[3]))

    print("Travel Allowance: ₹{:.2f}".format(emp[4]))

    print("Gross Salary: ₹{:.2f}".format(emp[5]))

    print("PF (8%): ₹{:.2f}".format(emp[6]))

    print("Tax (5%): ₹{:.2f}".format(emp[7]))

    print("Total Deductions: ₹{:.2f}".format(emp[8]))

    print("NET SALARY: ₹{:.2f}".format(emp[9]))

    print("================================")


print("\n================================")
print("       PAYROLL SUMMARY")
print("================================")

print("Total Employees:", len(employees))

print("Total Gross Payroll: ₹{:.2f}".format(total_gross))

print("Total Deductions: ₹{:.2f}".format(total_deductions))

print("Total Net Payroll: ₹{:.2f}".format(total_net))

print("================================")