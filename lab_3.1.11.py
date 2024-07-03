income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
	
elif income > 85528: # using elif function to find if the income is greater that the number.
	tax = 14839.2 + (income - 85528) * 0.32 # tax calculation from the calculation

tax = round(tax, 0) # rounding tax to .0 

if tax < 0:
    tax = 0.0 # if tax is in minus the tax is equal to 0

print("The tax is:", tax, "thalers")