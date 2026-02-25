# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Read the number from the user.
2. Loop from 1 to n.
3. Print stars multiplied by loop number.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# My Solution

# Variables
rows: int = int(input("Enter the number of row you would like to have: \n"))

# Main Code
for row in range(1, rows + 1):
    print("⭐" * row)

