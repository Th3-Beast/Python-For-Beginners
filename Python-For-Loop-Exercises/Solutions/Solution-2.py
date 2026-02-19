# The solution to Exercise 2 - Count Even Numbers

# Write a program that reads how many numbers will follow,
# then counts how many of those numbers are even.
# Print the count of even numbers.

# Variables
count = int(input())
even_count = 0

# Main Code
for number in range(count):
  numbers = int(input())
  if numbers % 2 == 0:
    even_count += 1

print(even_count)