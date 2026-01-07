from cryptography.fernet import Fernet, InvalidToken # Fernet allows for Symmetric Encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # Derives strong keys from passwords
from cryptography.hazmat.backends import default_backend
import base64 # Encode/Decode for file storage
import os
import sys
from pathlib import Path

class FileEncryptor:
    def __init__(self):
        # initialize Encryptor
        self.backend = default_backend()

    def derive_key_from_password(self, password, salt=None):
        """Derive a cryptographic key from a password
        Args:
            password: User's password (string)
            salt: Random salt (or generate if None)
        Returns:
            (key, salt) - encryption key and salt used"""
        
        # Generate Salt if not provided
        if salt is None:
            salt = os.urandom(16)
        
        # Convert password to bytes
        if isinstance(password, str):
            password = password.encode()

        # Derive key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32, # 32 bytes = 256 bits for AES-256
            salt=salt,
            iterations=310000,
            backend=self.backend
        )

        # Generate key and encode for Fernet
        key = base64.urlsafe_b64encode(kdf.derive(password))

        return key, salt
    
    def encrypt_file(self, filepath, password):
        """ Encrypt a file
        Args:
            filepath: Path to file to encrypt
            password: Password for encryption
        Returns:
            True if successful, False otherwise"""
          
        try:
            # Verify that file exists
            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return False
            print(f"Encrypting {filepath}")

            # Read original file
            with open(filepath, 'rb') as f:
                original_data = f.read()

            # Derive key from password
            key, salt = self.derive_key_from_password(password)

            # Create a cipher
            cipher = Fernet(key)

            # Encrypt Data
            encrypted_data = cipher.encrypt(original_data)

            # Create Encrypted Filename
            encrypted_filepath = filepath + '.encrypted'

            # Write encrypted file with salt prepended
            # Format: [16-byte salt][encrypted data]
            with open(encrypted_filepath, 'wb') as f:
                f.write(salt + encrypted_data)
            
            print(f"Encryption successful!")
            print(f"Original: {filepath}")
            print(f"Encrypted: {encrypted_filepath}")
            
            # Delete original file
            response = input("Delete original file? (y/n): ")
            if response.lower() == 'y':
                os.remove(filepath)
                print("Original file deleted")
            
            return True
        
        except Exception as e:
            print(f"Encryption failed: {e}")
            return False
        
    def decrypt_file(self, filepath, password):
        """
        Decrypt a file
        
        Args:
            filepath: Path to encrypted file
            password: Password for decryption
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Verify file exists
            if not os.path.exists(filepath):
                print(f"File not found: {filepath}")
                return False
            
            print(f"Decrypting {filepath}...")
            
            # Read encrypted file
            with open(filepath, 'rb') as f:
                file_data = f.read()
            
            # Extract salt (first 16 bytes)
            salt = file_data[:16]
            encrypted_data = file_data[16:]
            
            # Derive key using stored salt
            key, _ = self.derive_key_from_password(password, salt)
            
            # Create cipher
            cipher = Fernet(key)
            
            # Decrypt data
            try:
                decrypted_data = cipher.decrypt(encrypted_data)
            except InvalidToken:
                print(f"Decryption failed: Wrong password or corrupted file")
                return False
            
            # Create decrypted filename
            if filepath.endswith('.encrypted'):
                decrypted_filepath = filepath[:-10]  # Remove '.encrypted'
            else:
                decrypted_filepath = filepath + '.decrypted'
            
            # Write decrypted file
            with open(decrypted_filepath, 'wb') as f:
                f.write(decrypted_data)
            
            print(f"Decryption successful!")
            print(f"Encrypted: {filepath}")
            print(f"Decrypted: {decrypted_filepath}")
            
            return True
        
        except Exception as e:
            print(f"Decryption failed: {e}")
            return False
    
    def get_file_info(self, filepath):
        """Display file information"""
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return
        
        size = os.path.getsize(filepath)
        print(f"\n{'='*50}")
        print(f"File: {filepath}")
        print(f"Size: {size:,} bytes ({size/1024:.2f} KB)")
        print(f"{'='*50}\n")

def display_menu():
    """Display main menu"""
    print(f"\n{'='*50}")
    print("FILE ENCRYPTION/DECRYPTION TOOL")
    print(f"{'='*50}")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. File information")
    print("4. Exit")
    print(f"{'='*50}")
    return input("Select option (1-4): ")

def encrypt_interactive(encryptor):
    """Interactive encryption"""
    filepath = input("Enter file path to encrypt: ").strip()
    
    # Verify file exists
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    # Get password
    print("Enter a strong password (8+ characters)")
    password = input("Password: ")
    
    if len(password) < 8:
        print("Password too short (minimum 8 characters)")
        return
    
    # Confirm password
    password_confirm = input("Confirm password: ")
    if password != password_confirm:
        print("Passwords don't match")
        return
    
    # Encrypt
    encryptor.encrypt_file(filepath, password)

def decrypt_interactive(encryptor):
    """Interactive decryption"""
    filepath = input("Enter encrypted file path: ").strip()
    
    # Verify file exists
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    
    # Get password
    password = input("Enter decryption password: ")
    
    # Decrypt
    encryptor.decrypt_file(filepath, password)

def main():
    """Main program"""
    encryptor = FileEncryptor()
    
    print(f"\n{'='*50}")
    print("FILE ENCRYPTION/DECRYPTION TOOL")
    print("Educational Project - AES-256 Encryption")
    print(f"{'='*50}")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            encrypt_interactive(encryptor)
        elif choice == "2":
            decrypt_interactive(encryptor)
        elif choice == "3":
            filepath = input("Enter file path: ").strip()
            encryptor.get_file_info(filepath)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()