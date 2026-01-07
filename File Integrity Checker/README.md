# File Integrity Checker
Welcome to my file integrity checker project. The purpose of this project is to design a file integrity verification tool in Python to gain a better understanding of how file hashing works and to detect unauthorized modifications to sensitive files.

## How to use
### file_integrity_checker.py:
Before running, make sure you do pip install hashlib (usually built-in) or just run directly.

The program provides an interactive menu to create file checksums and verify file integrity using SHA-256 hashing.

### Features:

Calculate file checksums (MD5, SHA-256, SHA-512)

Store checksums in a database

Verify file integrity by comparing checksums

Detect if files have been modified

Export integrity reports

Monitor multiple files at once

### Steps to use:

1. Run the program with python3 file_integrity_checker.py

2. Select option 1 to calculate a file checksum

3. Choose your hash algorithm (SHA-256 recommended)

4. Enter the file path

5. The checksum will be stored in integrity_database.json

6. To verify integrity, select option 2

7. The program will compare the current checksum with the stored one

8. Any modifications will be detected and reported

### Security Features:

SHA-256 hashing (cryptographically secure)

Persistent checksum storage

Timestamp tracking

Modification detection

JSON database for easy management

Support for multiple hash algorithms

Once finished, check the integrity_database.json file to view all stored checksums.

### This project was developed as part of a cybersecurity learning initiative to understand file integrity verification and intrusion detection methods.

### This project is not intended to be used maliciously. If you do that, shame on you. >:(
