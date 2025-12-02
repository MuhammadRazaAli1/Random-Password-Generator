# Password Generator
Welcome to the Password Generator, a robust security tool built entirely in Python using a simple and interactive command-line interface (CLI). This project demonstrates core Python fundamentals like random selection, loops, string manipulation, conditional logic, and user input validation.

## Project Overview
Password Generator is a lightweight utility designed to create strong, randomized passwords for enhanced security. The application generates secure passwords by randomly selecting characters from a diverse pool of letters (uppercase and lowercase), numbers, and special symbols. Users can specify their desired password length, ensuring flexibility and customization for different security requirements.

## Features
* Random character selection from a comprehensive character set
* Support for uppercase and lowercase letters
* Inclusion of numeric characters (0-9)
* Inclusion of special symbols for enhanced security (!@#-)
* User-defined password length customization
* Input validation with length constraints (maximum 15 characters)
* Real-time password generation and display
* Clear feedback messages for validation errors
* Beginner-friendly, clean, and readable Python code
* Instant generation with immediate user feedback

## How It Works
* The program displays a prompt asking for the desired password length.
* The user enters a numeric value for the password length.
* The application validates the input against the maximum length constraint (15 characters).
* If valid, the program generates a password by randomly selecting characters.
* Random characters are selected from a predefined character set containing letters, numbers, and symbols.
* The generated password is displayed to the user.
* If invalid, the program displays an error message and prompts the user to try again.

## Character Set
The password generator uses a diverse character pool for maximum security:
* **Uppercase Letters:** A-Z
* **Lowercase Letters:** a-z
* **Numbers:** 0-9
* **Special Symbols:** ! @ # -

## Example Usage
```
Enter Password Length: 12
Your Password: a7!KpQ#mXz9@B

Enter Password Length: 20
Password length should be at least 15 characters or less.
Try Again!
```

## Concepts Used
* random.choice() for selecting random elements from a sequence
* String concatenation for building the password
* Loops (for) for iterating and generating password characters
* Conditional logic (if-else) for input validation
* User input handling through input() function
* String formatting with f-strings for dynamic output
* Character sets and string manipulation
* Validation constraints for security best practices
* User interaction through CLI (Command-Line Interface)
