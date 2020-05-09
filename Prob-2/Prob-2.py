# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Filipp Kopytyuk

'''
Input: Person's name, person's hourly wage, person's hours
Process: if worked more than fourty hours, get paid time and a half of all wages
Output: employee's name, regular wages, overtime wages, total wages, tax withholding, 
        insurance withholding, take home pay.
'''

def main():
    # employee info:
    name = (input("Enter your name:"))
    hourlyWage = float(input("Enter hourly wage:"))
    hours = int(input("Enter hours:"))

    # Normal wages
    normalWage = hourlyWage * hours
    print(normalWage)

    # Overtime wages
    overtimeWage = (hours - 40) * 1.5 
    print(overtimeWage)

    # Total wages
    totalWage = normalWage + overtimeWage
    print(totalWage)

    # Tax withholding
    tax = totalWage * 0.2
    print(tax)

    # Insurance withholding
    insurance = totalWage * 0.1
    print(insurance)

    # Take home pay
    homePay = totalWage - tax - insurance
    print(homePay)
    print()

    # Paycheck information
    print("Employee name: ", name)
    print("Normal wage: ", normalWage)
    print("Overtime wage: ", overtimeWage)
    print("Total wage: ", totalWage)
    print("Tax withholdings: ", tax)
    print("Insurance withholding: ", insurance)
    print("Take home pay: ", homePay)
    print()

main()