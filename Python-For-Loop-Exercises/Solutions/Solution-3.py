# The solution to Exercise 3 - Find the Maximum

# Write a program that reads how many numbers will follow,
# then finds and prints the largest number among them.

# Variables
count: int = int(input())
max_number = -999999

# Main Code
for i in range(count):
    number: int = int(input())
    if number > max_number:
        max_number = number

print(max_number)
