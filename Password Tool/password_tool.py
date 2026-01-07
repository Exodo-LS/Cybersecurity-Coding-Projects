import re                       # Pattern matching for password validation
import string                   # String constants(uppercase, lowercase, digits, and symbols)
import secrets                  # Cryptographically secure random generation
from getpass import getpass     # Hide password input from screen

# Evaluate password strength and return score (0-100) and feedback
# Format: (score, feedback, strength_level)
def check_password_strength(password):
    score = 0
    feedback = []


    # Length Check
    # Worth 0 - 30 points total
    if len(password) >= 8:
        score += 5
        if len(password) >= 12:
            score += 15
            if len(password) >= 16:
                score += 20
                feedback.append("Password length more than 8 characters long with at least 16 characters")
            else:
                feedback.append("Password length more than 8 characters long with at least 12 characters")
        else:
            feedback.append("Password length is at least 8 characters long")
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase Check
    # Worth 0 - 15 points total
    if re.search(r"[A-Z]", password):
        score += 15
        feedback.append("Uppercase letters used")
    else:
        feedback.append("Add uppercase letters")

    # Lowercase Check
    # Worth 0 - 15 points total
    if re.search(r"[a-z]", password):
        score += 15
        feedback.append("Lowercase letters used")
    else:
        feedback.append("Add lowercase letters")

    # Number Check
    # Worth 0 - 15 points total
    if re.search(r"[0-9]", password):
        score += 15
        feedback.append("Numbers used")
    else:
        feedback.append("Add numbers")

    # Special Characters Check
    # Worth 0 - 15 points total
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 15
        feedback.append("Special characters used")
    else:
        feedback.append("Add special characters")    
    
    # Common Patterns Check
    # Penalty -10 points
    common_patterns = ["123", "abc", "password", "qwerty", "admin", "letmein", "123456", "123456789", "pass"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 10
        feedback.append("Avoid common patterns")
    else:
        feedback.append("No common patterns detected")
    
    # Determine strength level
    if score >= 80:
        strength = "STRONG"
    elif score >= 60:
        strength = "GOOD"
    elif score >= 40:
        strength = "FAIR"
    else:
        strength = "WEAK"
    
    return score, feedback, strength

# Generate a secure random password
# Args: length = 12 characters / toggles for character types
# Returns the generated password from the args
def generate_password(length=12, useUppercase=True, useLowercase=True, useNumbers=True, useSpChar=True):
    characters = ""

    if useUppercase:
        characters += string.ascii_uppercase
    if useLowercase:
        characters += string.ascii_lowercase
    if useNumbers:
        characters += string.digits
    if useSpChar:
        characters += "!@#$%^&*()_+-=[]{}:;\"'<>,.?/"

    # Validate that we have characters to generate password
    if not characters:
        return None
    
    # Generate a password with cryptographically safe random selection to avoid predictable patterns
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Batch Password Checking From File
# One per line
def batch_check_passwords():
    filename = input("Enter name of file with passwords:")

    try:
        with open(filename, 'r', encoding='latin-1') as f:
            passwords = f.readlines()

            print(f"\n{'='*50}")
            print(f"Analyzing {len(passwords)} passwords...")
        print(f"{'='*50}\n")
        
        for i, password in enumerate(passwords, 1):
            password = password.strip()
            if password:
                score, _, strength = check_password_strength(password)
                print(f"{i}. {password} {strength} (Score: {score}/100)")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Display Options
def display_menu():
    print("\n" + "="*50)
    print("PASSWORD SECURITY TOOL")
    print("="*50)
    print("1. Check Password Strength")
    print("2. Generate Secure Password")
    print("3. Batch Check Passwords (from file)")
    print("4. Exit")
    print("="*50)
    return input("Select option (1-4): ")

# Way to interact with the check_password function
def check_password_interactive():
    # Password input will be hidden
    password = getpass("Enter password to check: ")

    score, feedback, strength = check_password_strength(password)

    print(f"\n{'='*50}")
    print(f"Password: {password}")
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/100")
    print(f"{'='*50}")
    
    if feedback:
        print("Recommendations:")
        for item in feedback:
            print(f"  {item}")
    else:
        print("Excellent password! No improvements suggested.")

# Way to interact with the generate_password function
def generate_password_interactive():
    print("\n" + "="*50)
    print("PASSWORD GENERATOR")
    print("="*50)
    
    try:
        length = int(input("Password length (default 12): ") or 12)
        
        # Ensure reasonable length
        if length < 8 or length > 128:
            print("Password length must be between 8 and 128")
            return
        
        use_uppercase = input("Include uppercase? (y/n, default y): ").lower() != 'n'
        use_lowercase = input("Include lowercase? (y/n, default y): ").lower() != 'n'
        use_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
        
        password = generate_password(
            length=length,
            useUppercase=use_uppercase,
            useLowercase=use_lowercase,
            useNumbers=use_numbers,
            useSpChar=use_symbols
        )
        
        print(f"\n{'='*50}")
        print(f"Generated Password: {password}")
        print(f"{'='*50}")
        
        # Check strength of generated password
        score, feedback, strength = check_password_strength(password)
        print(f"Strength: {strength} (Score: {score}/100) Feedback: {feedback}" )
        
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            check_password_interactive()
        elif choice == "2":
            generate_password_interactive()
        elif choice == "3":
            batch_check_passwords()
        elif choice == "4":
            print("\n Thank you for using my password security tool!")
            break
        else:
            print("Invalid option!! Try Again!!")

if __name__ == "__main__":
    main()