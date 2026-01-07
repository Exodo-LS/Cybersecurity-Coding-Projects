# Password Tool

Welcome to my password tool project. The purpose of this project is to design a comprehensive password utility in Python to gain a better understanding of password security, generation, and validation techniques used in cybersecurity.

## How to use

### password_tool.py

Before running, make sure you have Python 3.6+ installed. No external dependencies needed!

The program provides an interactive menu with multiple password utilities including generation, validation, strength analysis, and hashing.

**Features:**
- Generate random passwords with custom specifications
- Validate password strength with detailed feedback
- Hash passwords using SHA-256 and bcrypt
- Test passwords against common dictionaries
- Create password policies for organizations
- Batch password generation
- Password expiration recommendations
- Cracking time estimation for given passwords
- Entropy calculation
- Dictionary attack simulation

**Steps to use:**
1. Run the program with `python3 password_tool.py`
2. Select option 1 to generate a random password
3. Specify length (recommended: 12+ characters)
4. Choose character types (uppercase, lowercase, numbers, symbols)
5. Use option 2 to check password strength
6. Enter a password to analyze
7. Get detailed feedback on strength, entropy, and recommendations
8. Use option 3 to hash a password with SHA-256
9. Use option 4 to test against common weak passwords
10. Use option 5 to estimate cracking time

**Password Generation Settings:**
- Length: 8-64 characters (12+ recommended for security)
- Character types: lowercase, uppercase, numbers, symbols
- Customizable exclude characters
- Cryptographically secure randomness
- No dictionary words by default

**Password Strength Criteria:**
- **Very Weak:** < 8 characters, no variety
- **Weak:** 8-12 characters, limited variety
- **Fair:** 12-16 characters, good variety
- **Strong:** 16+ characters, all types, no patterns
- **Very Strong:** 16+ characters, high entropy, random

**Security Metrics Provided:**
- Entropy (bits of randomness)
- Estimated cracking time
- Character variety score
- Pattern analysis
- Dictionary word detection
- Common password detection
- Sequential character detection

**Recommendations:**
- Use 12-16 character passwords minimum
- Mix uppercase, lowercase, numbers, and symbols
- Avoid dictionary words and personal information
- Change passwords regularly (90 days recommended)
- Use unique passwords for each service
- Enable two-factor authentication when available
- Never reuse passwords across accounts

Once finished, use the generated passwords or implement the validation checks in your own projects.

## Credit

This project was developed as part of a cybersecurity learning initiative to understand password security principles and best practices.

This project is not intended to be used maliciously. If you do that, shame on you. >:(
