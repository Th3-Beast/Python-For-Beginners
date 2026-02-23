# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Loop from 1 to n.
2. Check divisibility carefully.
3. Order matters when checking both 3 and 5.
4. Print correct value each iteration.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# Variables
my_number: int = int(input("What number would you like to count to: \n"))

# Main Code
for number in range(1, my_number + 1):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	else:
		print(number)
