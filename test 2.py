# Read the number of blocks from the user
blocks = int(input("Enter the number of blocks: "))

# Initialize variables to keep track of the current height and the number of blocks needed for the next layer
height = 0
blocks_needed = 1

# Loop to build the pyramid
while blocks >= blocks_needed:
    # Build the current layer
    blocks -= blocks_needed
    # Move to the next layer
    height += 1
    # The next layer will require one more block than the current one
    blocks_needed += 1

# Output the height of the pyramid
print("The height of the pyramid:", height)
