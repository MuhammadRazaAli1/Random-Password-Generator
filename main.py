import random  # Importing random module for random character selection

# Define the set of characters to choose from (letters, numbers, and symbols)
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#-"

# Ask user for the desired password length
characters_length = int(input("Enter Password Length: "))

# Initialize an empty string to store the generated password
password = ""

# Loop through the range of desired length and add random characters
for i in range(characters_length):
    password += random.choice(characters)

# Check if the password length exceeds 15 characters
if characters_length > 15:
    print("Password length should be at least 15 charaters or less.")
    print("Try Again!")
else:
    print(f"Your Password: {password}") # Display the generated password
