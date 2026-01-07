# File Encryptor
Welcome to my file encryptor project. The purpose of this project is to design a file encryption tool in Python to gain a better understanding of how encryption works and to securely protect sensitive files.

## How to use
### file_encryptor.py:
Before running, make sure you do pip install cryptography

The program provides an interactive menu to encrypt and decrypt files using AES-256 encryption with PBKDF2 key derivation.

Features:

Encrypt files with a strong password

Decrypt encrypted files

View file information

Persistent storage with salt included in encrypted files

Steps to use:

Run the program with python3 file_encryptor.py

Select option 1 to encrypt a file

Enter the file path you want to encrypt

Create a strong password (8+ characters)

Confirm your password

Your file will be encrypted with .encrypted extension

To decrypt, select option 2 and enter the encrypted file path and password

Security Features:

AES-256 encryption (Fernet)

PBKDF2 key derivation with 100,000 iterations

Random salt generation and storage

Password confirmation on creation

Error handling for wrong passwords

Once finished, check for the encrypted file in your directory.

Credit
This project was developed as part of a cybersecurity learning initiative to understand encryption fundamentals and secure file protection methods.

This project is not intended to be used maliciously. If you do that, shame on you. >:(
