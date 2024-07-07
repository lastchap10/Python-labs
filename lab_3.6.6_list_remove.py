my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Create an empty list to store unique numbers
unique_list = []

# Iterate through the original list
for number in my_list:
    # If the number is not already in the unique list, add it
    if number not in unique_list:
        unique_list.append(number)

# Print the result
print("The list with unique elements only:", unique_list)
print(my_list)