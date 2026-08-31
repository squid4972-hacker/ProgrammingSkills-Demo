"""
Program: practicetaxform.py
Author: Enaya Laborn
Compute a person's tax income.
"""
# Initializing values
STANDARD_DEDUCT = 10000.0
DEPENDENT_DEDUCT = 3000.0
TAX_RATE = 0.20

# Compute the income tax
grossIncome = float(input("Enter gross income: "))
noDep = int(input("Enter the number of dependents: "))
taxableIncome = grossIncome - STANDARD_DEDUCT - (DEPENDENT_DEDUCT * noDep)
incomeTax = taxableIncome * TAX_RATE

#Display the income tax (and a small joke to make taxes a little more bearable)
print("The income tax is $" + str(incomeTax) +
      "\nWould you like to pay with cash, check, or wage garnishments?\nPay or go to prison!")


