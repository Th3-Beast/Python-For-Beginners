# =============================================
# The Solution
# =============================================

# ------------------------------
# Detailed Breakdown
# ------------------------------
"""
1. Read a string.
2. Loop through each character.
3. Check if it is a vowel.
4. Count matches.
5. Print the result.
"""
# =============================================

# ------------------------------
# My Solution
# ------------------------------

# My Solution

# Variables
user_word: str = input("Enter the word you would like to check: \n").lower()
vowel_count: int = 0
vowels: str = "aeiou"

# Main Code
for letter in user_word:
    if letter in vowels:
        vowel_count += 1

print(vowel_count)
