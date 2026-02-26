# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Loop from 1 to n.
2. Inside loop, build a string.
3. Append numbers from 1 to current row.
4. Print the string.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# My Solution

# Variables
rows: int = int(input("What number do you want to count upto?\n"))

# Main Code
for row in range(1, rows + 1):
    line: str = ""
    for column in range(1, row + 1):
        line += str(column)
    print(line)

