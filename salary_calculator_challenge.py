# Day 1 – Main Lab CHALLENGE version
# Processes many employees in a loop until the user types "exit",
# deducts PF at 12% of basic, shows net salary, and prints the total payroll.
# Still Day 1 concepts only: no functions, no lists.
#
# Run:  python salary_calculator_challenge.py

HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12

employee_count = 0
total_gross = 0.0
total_net = 0.0

while True:
    name = input("\nEmployee name (or 'exit' to finish): ").strip()
    if name.lower() == "exit":
        break
    if name == "":
        print("  Name cannot be empty.")
        continue
    name = name.title()

    while True:
        basic_text = input("Basic salary: ").strip()
        if basic_text.replace(".", "", 1).isdigit() and float(basic_text) > 0:
            basic = float(basic_text)
            break
        print("  Please enter a positive number, e.g. 50000")

    while True:
        experience_text = input("Years of experience: ").strip()
        if experience_text.isdigit():
            experience = int(experience_text)
            break
        print("  Please enter a whole number 0 or more, e.g. 4")

    hra = basic * HRA_RATE
    da = basic * DA_RATE

    if experience < 2:
        bonus_rate = 0.05
    elif experience <= 5:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.15

    bonus = basic * bonus_rate
    gross = basic + hra + da + bonus
    pf = basic * PF_RATE
    net = gross - pf

    if gross >= 100000:
        category = "High"
    elif gross >= 50000:
        category = "Medium"
    else:
        category = "Low"

    bonus_label = "Bonus (" + str(int(bonus_rate * 100)) + "%)"
    print("=" * 40)
    print(f"{'SALARY REPORT':^40}")
    print("=" * 40)
    print(f"{'Name':<20}{name:>20}")
    print(f"{'Experience':<20}{str(experience) + ' years':>20}")
    print(f"{'Basic':<20}{basic:>20,.2f}")
    print(f"{'HRA (20%)':<20}{hra:>20,.2f}")
    print(f"{'DA (10%)':<20}{da:>20,.2f}")
    print(f"{bonus_label:<20}{bonus:>20,.2f}")
    print("-" * 40)
    print(f"{'Gross Salary':<20}{gross:>20,.2f}")
    print(f"{'PF (12%)':<20}{-pf:>20,.2f}")
    print(f"{'Net Salary':<20}{net:>20,.2f}")
    print(f"{'Category':<20}{category:>20}")
    print("=" * 40)

    employee_count += 1
    total_gross += gross
    total_net += net

print()
if employee_count == 0:
    print("No employees entered.")
else:
    print(f"Employees processed : {employee_count}")
    print(f"Total gross payroll : {total_gross:,.2f}")
    print(f"Total net payroll   : {total_net:,.2f}")
