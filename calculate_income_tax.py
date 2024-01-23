# Exercise 12: Calculate income tax for the given income by adhering to the rules below

income = 120000
tax_payable = 0
print("Your income", income)

if income <= 5000:
    tax_payable = 0
elif income <= 10000:
    # no tax on first 5,000
    x = income - 5000
    # 10% tax
    tax_payable = x * 10 / 100
