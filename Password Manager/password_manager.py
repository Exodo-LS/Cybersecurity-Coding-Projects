from cryptography.fernet import Fernet
import json
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


class PasswordManager:
    def __init__(self, master_password):
        """Initialize password manager with master password"""
        self.master_key = self.derive_key(master_password)
        self.cipher = Fernet(self.master_key)
        self.passwords = {}
        self.load_passwords()
    
    def derive_key(self, password):
        """Derive encryption key from master password"""
        salt = b'salt1234'  # In production, use random salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=310000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def add_password(self, service, username, password):
        """Add encrypted password"""
        entry = f"{username}:{password}"
        encrypted = self.cipher.encrypt(entry.encode())
        self.passwords[service] = encrypted
        self.save_passwords()
        print(f"Password saved for {service}")
        return True
    
    def get_password(self, service):
        """Retrieve decrypted password"""
        if service not in self.passwords:
            print(f"No password for {service}")
            return None
        
        try:
            encrypted = self.passwords[service]
            decrypted = self.cipher.decrypt(encrypted).decode()
            username, password = decrypted.split(':')
            
            print(f"\n{'='*50}")
            print(f"Password for {service}")
            print(f"{'='*50}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"{'='*50}\n")
            return True
        except Exception as e:
            print(f"Error retrieving password: {e}")
            return False
    
    def list_services(self):
        """List all stored services"""
        if not self.passwords:
            print("No passwords stored")
            return
        
        print(f"\n{'='*50}")
        print("STORED SERVICES")
        print(f"{'='*50}")
        for i, service in enumerate(self.passwords.keys(), 1):
            print(f"{i}. {service}")
        print(f"{'='*50}\n")
    
    def delete_password(self, service):
        """Delete a stored password"""
        if service not in self.passwords:
            print(f"No password for {service}")
            return False
        
        confirm = input(f"Delete password for {service}? (y/n): ").lower()
        if confirm == 'y':
            del self.passwords[service]
            self.save_passwords()
            print(f"Password for {service} deleted")
            return True
        else:
            print("Delete cancelled")
            return False
    
    def save_passwords(self):
        """Save encrypted passwords"""
        data = {k: v.decode() for k, v in self.passwords.items()}
        with open('passwords.json', 'w') as f:
            json.dump(data, f)
    
    def load_passwords(self):
        """Load encrypted passwords"""
        if os.path.exists('passwords.json'):
            try:
                with open('passwords.json', 'r') as f:
                    data = json.load(f)
                    self.passwords = {k: v.encode() for k, v in data.items()}
            except Exception as e:
                print(f"Error loading passwords: {e}")


def display_menu():
    """Display main menu"""
    print(f"\n{'='*50}")
    print("PASSWORD MANAGER")
    print(f"{'='*50}")
    print("1. Add password")
    print("2. Retrieve password")
    print("3. List all services")
    print("4. Delete password")
    print("5. Exit")
    print(f"{'='*50}")
    return input("Select option (1-5): ")


def add_password_interactive(manager):
    """Interactive password addition"""
    print(f"\n{'='*50}")
    print("ADD NEW PASSWORD")
    print(f"{'='*50}")
    
    service = input("Service name (e.g., Gmail, GitHub): ").strip()
    if not service:
        print("Service name cannot be empty")
        return
    
    username = input("Username/Email: ").strip()
    if not username:
        print("Username cannot be empty")
        return
    
    password = input("Password: ").strip()
    if not password:
        print("Password cannot be empty")
        return
    
    # Confirm password
    password_confirm = input("Confirm password: ").strip()
    if password != password_confirm:
        print("Passwords don't match")
        return
    
    manager.add_password(service, username, password)


def retrieve_password_interactive(manager):
    """Interactive password retrieval"""
    service = input("Enter service name: ").strip()
    
    if not service:
        print("Service name cannot be empty")
        return
    
    manager.get_password(service)


def delete_password_interactive(manager):
    """Interactive password deletion"""
    service = input("Enter service name to delete: ").strip()
    
    if not service:
        print("Service name cannot be empty")
        return
    
    manager.delete_password(service)


def main():
    """Main program loop"""
    print(f"\n{'='*50}")
    print("PASSWORD MANAGER")
    print("Secure Password Storage Tool")
    print(f"{'='*50}\n")
    
    # Get master password
    master_password = input("Enter master password: ").strip()
    
    if len(master_password) < 8:
        print("Master password must be at least 8 characters")
        return
    
    manager = PasswordManager(master_password)
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_password_interactive(manager)
        elif choice == "2":
            retrieve_password_interactive(manager)
        elif choice == "3":
            manager.list_services()
        elif choice == "4":
            delete_password_interactive(manager)
        elif choice == "5":
            print("\nThank you for using Password Manager!")
            break
        else:
            print("Invalid option. Please try again.")


# Program entry point
if __name__ == "__main__":
    main()