# Password Manager

Welcome to my password manager project. The purpose of this project is to design a secure password management tool in Python to gain a better understanding of how password managers work and to learn proper password storage and encryption techniques.

## How to use

### password_manager.py:

Before running, make sure you do `pip install cryptography`

The program provides an interactive menu to securely store, retrieve, and manage passwords using AES-256 encryption and secure hashing.

**Features:**
- Add new password entries with username, password, and service name
- Retrieve stored passwords securely
- List all stored password entries (usernames and services only)
- Delete password entries
- Search for passwords by service or username
- Export encrypted password database
- Import existing password databases
- Master password protection with hashing
- Secure password generation recommendations
- Password strength assessment

**Steps to use:**
1. Run the program with `python3 password_manager.py`
2. Create a master password on first run (this protects all your passwords)
3. Select option 1 to add a new password
4. Enter the service name (e.g., "Gmail", "GitHub")
5. Enter your username for that service
6. Enter your password (or let the program suggest a strong one)
7. Use option 2 to retrieve a password (enter master password)
8. Use option 3 to view all stored services
9. Use option 4 to delete an entry
10. Use option 5 to change your master password

**Security Features:**
- AES-256 encryption for all stored passwords
- Master password protection with PBKDF2 hashing
- Secure password generation with cryptographic randomness
- Password strength checking (minimum 8 characters recommended)
- Encrypted database storage
- Session timeout for security
- Secure deletion of sensitive data from memory

**Password Database:**
- Stored in `passwords.db` (encrypted JSON format)
- Master password hash stored in `master.key`
- Never store plaintext passwords
- All passwords encrypted before storage

**Password Strength Requirements:**
- Minimum 8 characters
- Mix of uppercase, lowercase, numbers, and symbols recommended
- Avoid dictionary words
- Use unique passwords for each service

Once finished, your passwords are securely encrypted and stored locally on your system.

## Credit

This project was developed as part of a cybersecurity learning initiative to understand password management best practices and encryption techniques.

This project is not intended to be used maliciously. If you do that, shame on you. >:(
