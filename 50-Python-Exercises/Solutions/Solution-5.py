# The solution to Exercise 5 - Average Calculator

# Write a program that reads how many numbers will follow,
# then calculates and prints the average of those numbers.

# My Solution

# Variables
count: int = int(input())
total = 0

# Main Code
for number in range(count):
    new_number: int = int(input())
    total += new_number

avg = total / count

print(avg)