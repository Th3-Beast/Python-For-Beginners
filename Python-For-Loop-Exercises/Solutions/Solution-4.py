# The solution to Exercise 4 - Find the Minimum

# Write a program that reads how many numbers will follow,
# then finds and prints the smallest number among them.

# Variables
count = int(input())
min_number = 999999

# Main Code
for i in range(count):
    number = int(input())
    if number < min_number:
        min_number = number
print(min_number)
