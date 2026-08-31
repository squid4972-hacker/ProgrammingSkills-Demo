"""
Author: Enaya S. laborn
Date: 30 August 2026
This program is a simple program to calculate an employee's total weekly pay
by calculating hourly wage, time worked, and will calculate overtime pay as well.
"""

hrWork = float(input("Enter hours worked this week: "))
hrWage = float(input("Enter hourly wage: "))
OT_WAGE = 1.5 * hrWage

if hrWork <= 40:
    print("Your estimated gross weekly pay is " + str(hrWork * hrWage))
else:
    otHours = hrWork - 40
    otPremium = otHours * OT_WAGE
    basePay = (40 * hrWage)
    totalPay = (otPremium + basePay)
    print(f"""Your estimated gross weekly pay is {str(totalPay)}
""")


