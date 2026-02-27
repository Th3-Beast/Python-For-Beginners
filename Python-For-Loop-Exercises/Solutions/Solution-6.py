# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Read sentence.
2. Track whether inside a word.
3. Increase count when new word starts.
4. Print total.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# My Solution

# Variables
sentence: str = input("Add your sentence that you would like to count: \n")
count: int = 0
in_word: bool = False

# Main Code
for char in sentence:
    if char != " " and not in_word:
        count += 1
        in_word=True
    elif char == " ":
        in_word = False

print(count)

