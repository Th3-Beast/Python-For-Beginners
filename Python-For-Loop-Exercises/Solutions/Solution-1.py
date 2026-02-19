# The solution to Exercise 1 - Sum Of N Numbers

# Write a program that gets 3 input values from the user.
# The first input tells you how many numbers will follow.
# The next 2 inputs should be whole numbers, that you need to sum.
# Print the sum of all the input numbers (not including the first input).

# Variables
count = int(input())
total = 0

# Main Code
for numbers in range(count):
    number = int(input())
    total += number

print(total)
