import hashlib
import os


class FileIntegrityChecker:
    def __init__(self, database_file="file_hashes.txt"):
        """Initialize the file integrity checker"""
        self.database_file = database_file
        self.hashes = {}
        self.load_hashes()
    
    def calculate_hash(self, filepath):
        """Calculate SHA-256 hash of a file"""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def monitor_file(self, filepath):
        """Add file to monitoring"""
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return False
        
        file_hash = self.calculate_hash(filepath)
        self.hashes[filepath] = file_hash
        self.save_hashes()
        print(f"Now monitoring: {filepath}")
        return True
    
    def check_file(self, filepath):
        """Check if file has been modified"""
        if filepath not in self.hashes:
            print(f"File not being monitored: {filepath}")
            return False
        
        current_hash = self.calculate_hash(filepath)
        original_hash = self.hashes[filepath]
        
        if current_hash == original_hash:
            print(f"{filepath} - NO CHANGES DETECTED")
            return True
        else:
            print(f"ALERT! {filepath} HAS BEEN MODIFIED")
            print(f"Original hash: {original_hash}")
            print(f"Current hash:  {current_hash}")
            return False
    
    def check_all(self):
        """Check all monitored files"""
        if not self.hashes:
            print("No files being monitored")
            return
        
        print(f"\n{'='*50}")
        print("CHECKING ALL MONITORED FILES")
        print(f"{'='*50}\n")
        
        all_clean = True
        for filepath in self.hashes:
            current_hash = self.calculate_hash(filepath)
            original_hash = self.hashes[filepath]
            
            if current_hash == original_hash:
                print(f"{filepath} - NO CHANGES")
            else:
                print(f"{filepath} - MODIFIED!")
                all_clean = False
        
        print(f"\n{'='*50}")
        if all_clean:
            print("All files are secure")
        else:
            print("Some files have been modified")
        print(f"{'='*50}\n")
    
    def list_monitored_files(self):
        """List all monitored files"""
        if not self.hashes:
            print("No files being monitored")
            return
        
        print(f"\n{'='*50}")
        print("MONITORED FILES")
        print(f"{'='*50}")
        for i, filepath in enumerate(self.hashes.keys(), 1):
            print(f"{i}. {filepath}")
        print(f"{'='*50}\n")
    
    def save_hashes(self):
        """Save hashes to file"""
        with open(self.database_file, 'w') as f:
            for filepath, file_hash in self.hashes.items():
                f.write(f"{filepath}|{file_hash}\n")
    
    def load_hashes(self):
        """Load hashes from file"""
        if os.path.exists(self.database_file):
            with open(self.database_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        filepath, file_hash = line.split('|')
                        self.hashes[filepath] = file_hash


def display_menu():
    """Display main menu"""
    print(f"\n{'='*50}")
    print("FILE INTEGRITY CHECKER")
    print(f"{'='*50}")
    print("1. Monitor a file")
    print("2. Check a file")
    print("3. Check all files")
    print("4. List monitored files")
    print("5. Exit")
    print(f"{'='*50}")
    return input("Select option (1-5): ")


def monitor_file_interactive(checker):
    """Interactive file monitoring"""
    filepath = input("Enter file path to monitor: ").strip()
    
    if not filepath:
        print("No file path entered")
        return
    
    checker.monitor_file(filepath)


def check_file_interactive(checker):
    """Interactive file checking"""
    filepath = input("Enter file path to check: ").strip()
    
    if not filepath:
        print("No file path entered")
        return
    
    checker.check_file(filepath)


def main():
    """Main program loop"""
    print(f"\n{'='*50}")
    print("FILE INTEGRITY CHECKER")
    print("Detect Unauthorized File Modifications")
    print(f"{'='*50}\n")
    
    checker = FileIntegrityChecker()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            monitor_file_interactive(checker)
        elif choice == "2":
            check_file_interactive(checker)
        elif choice == "3":
            checker.check_all()
        elif choice == "4":
            checker.list_monitored_files()
        elif choice == "5":
            print("\nThank you for using File Integrity Checker!")
            break
        else:
            print("Invalid option. Please try again.")


# Program entry point
if __name__ == "__main__":
    main()