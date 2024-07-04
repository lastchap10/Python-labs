# Read the number of blocks from the user
blocks = int(input("Enter the number of blocks: "))

# Initialize variables for the height and the current layer
height = 0
current_layer = 1

# Build the pyramid layer by layer
while blocks >= current_layer:
    blocks -= current_layer
    height += 1
    current_layer += 1

# Output the height of the pyramid
print("The height of the pyramid:", height)
