x = float(input("Enter value for x: "))

# Given value for x

# Step-by-step calculation
inner_most = 1.0 / x                   # 1./x
second_inner = x + inner_most          # x + 1./x
third_inner = 1.0 / second_inner       # 1./(x + 1./x)
fourth_inner = x + third_inner         # x + 1./(x + 1./x)
fifth_inner = 1.0 / fourth_inner       # 1./(x + 1./(x + 1./x))
sixth_inner = x + fifth_inner          # x + 1./(x + 1./(x + 1./x))
y = 1.0 / sixth_inner                  # 1./(x + 1./(x + 1./(x + 1./x)))

print(y)


print("y =", y)

