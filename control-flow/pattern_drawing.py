# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle rows
while row < size:
    # Inner for loop to print asterisks in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after a row is complete
    row += 1
