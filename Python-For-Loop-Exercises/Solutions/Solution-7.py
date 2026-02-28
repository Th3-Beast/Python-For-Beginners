# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Read the number.
2. Assume the number is prime initially.
3. If the number is less than 2, mark it as not prime.
4. Loop from 2 up to one less than the number.
5. If the number is divisible by any value in that range:
    - Mark it as not prime.
    - Stop the loop.
6. After the loop, print "Prime" or "Not Prime" based on the result.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# My Solution

# Variables
number: int = int(input("Enter a number: "))
is_prime: bool = True

# Main Code
if number < 2:
    is_prime = False
else:
    # Check for factors from 2 up to the number
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
