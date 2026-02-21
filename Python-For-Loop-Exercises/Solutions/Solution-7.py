# The solution to Exercise 7 - Multiply All Numbers

# Write a program that reads how many numbers will follow,
# then multiplies all those numbers together and prints the result.

# My Solution

# Variables
count: int = int(input())
total: int = 1  # Remember to set this to 1 and not 0

# Main Code
for number in range(count):
    new_numbers: int = int(input())
    total *= new_numbers

print(total)