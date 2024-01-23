# Exercise 12: Calculate income tax for the given income by adhering to the rules below

income = 150000
tax_payable = 0
print("Your income:", income)

if income <= 5000:
    tax_payable = 0
elif income <= 10000:
    # first 5,000 no tax
    x = income - 5000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 5,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is:", tax_payable)