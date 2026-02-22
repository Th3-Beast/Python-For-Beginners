# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Read the maximum number.
2. Loop from 1 to that number.
3. Check if a number is odd.
4. Print it if it is.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

limit: int = int(input())

for number in range(1, limit + 1):
    if number % 2 != 0:
        print(number)
