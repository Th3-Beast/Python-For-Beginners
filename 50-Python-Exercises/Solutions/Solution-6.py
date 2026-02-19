# The solution to Exercise 6 - Count Positive Numbers

# Write a program that reads how many numbers will follow,
# then counts how many of those numbers are positive (greater than 0). Print the count.

# My Solution

# Variables
count: int = int(input())
counter = 0

# Main Code
for number in range(count):
    new_number: int = int(input())
    if new_number > 0:
        counter += 1

print(counter)