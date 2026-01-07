# Python Keylogger

Welcome to my keylogger project. The purpose of this project is to design a keylogger in Python to gain a better understanding on how these attacks work and to learn about system-level input monitoring for security research.

## How to use

### keylogger.py

Before running, make sure you do `pip install pynput`

The program provides an interactive menu-driven interface to start logging, view logs, and clear logs. It uses the Python `logging` module with timestamps and pynput for keyboard event capture.

**Features:**
- Interactive menu system with 4 options
- Class-based KeyLogger architecture for clean code
- Real-time keyboard input capture using pynput library
- Automatic file creation (keylog.txt by default)
- Timestamp logging for each keystroke (YYYY-MM-DD HH:MM:SS format)
- Progress tracking (shows keystroke count every 20 keys)
- Special key handling (Enter, Backspace, Tab, Space, Shift, Ctrl, Alt, Caps Lock)
- ESC key to stop logging and return to menu
- View last 50 logged keystrokes in reverse chronological order
- Clear log file functionality with confirmation
- Educational confirmation before starting (prevents accidental use)
- Comprehensive error handling for file operations
- Customizable log file name

**Steps to use:**

1. Run the program with `python3 keylogger.py`
2. Read the educational warning about legal use
3. Confirm you understand this is for educational purposes only (type 'y')
4. You'll see the main menu with 4 options:
   - **Option 1: Start keylogger** - Begins listening to keyboard input
   - **Option 2: View logs** - Displays the last 50 logged keystrokes
   - **Option 3: Clear logs** - Deletes the log file
   - **Option 4: Exit** - Closes the program
5. Select option 1 to start monitoring
6. A `keylog.txt` file will be created in your current directory
7. Press ESC key to stop logging and return to menu
8. Use option 2 to view captured keystrokes
9. Use option 3 to clear logs if desired
10. Select option 4 to exit the program

**Log File Output Example:**
```
2026-01-07 21:35:14,123 - INFO: KEY: P
2026-01-07 21:35:14,145 - INFO: KEY: a
2026-01-07 21:35:14,167 - INFO: KEY: s
2026-01-07 21:35:14,189 - INFO: KEY: s
2026-01-07 21:35:14,211 - INFO: KEY: w
2026-01-07 21:35:14,233 - INFO: KEY: o
2026-01-07 21:35:14,255 - INFO: KEY: r
2026-01-07 21:35:14,277 - INFO: KEY: d
2026-01-07 21:35:15,299 - INFO: [SPACE]
2026-01-07 21:35:15,321 - INFO: KEY: 1
2026-01-07 21:35:15,343 - INFO: KEY: 2
2026-01-07 21:35:15,365 - INFO: KEY: 3
2026-01-07 21:35:16,387 - INFO: [ENTER]
```

**What Gets Logged:**
- Individual keystroke characters (logged as "KEY: x")
- Special keys with descriptive names:
  - [ENTER] - Return key
  - [BACKSPACE] - Backspace key
  - [TAB] - Tab key
  - [SPACE] - Space key
  - [SHIFT] - Shift key
  - [CTRL] - Control key (left or right)
  - [ALT] - Alt key (left or right)
  - [CAPS_LOCK] - Caps Lock key
  - [Other keys with their names in brackets]
- Full timestamp with date and time (YYYY-MM-DD HH:MM:SS format)
- Keystroke counter for progress (printed every 20 keys)
- Total keystroke count before stopping

**Code Architecture:**

The program uses a `KeyLogger` class with these methods:

- `__init__(log_file)` - Initializes the keylogger with a log file name
- `on_press(key)` - Handles key press events and logs them
- `on_release(key)` - Handles key release events (checks for ESC to stop)
- `start()` - Begins listening to keyboard input with listener
- `stop()` - Stops the listener
- `view_logs()` - Displays the last 50 logged keystrokes
- `clear_logs()` - Removes the log file
- `display_menu()` - Shows the interactive menu
- `main()` - Main program loop

**Technical Details:**
- Uses `pynput.keyboard.Listener` for cross-platform support
- Uses Python's built-in `logging` module for file output
- Works on Windows, macOS, and Linux
- Non-blocking background listener
- Minimal CPU and memory usage
- Python 3.6+ compatible
- Handles keyboard events with proper exception handling

## ⚠️ CRITICAL LEGAL WARNING

**UNAUTHORIZED KEYLOGGING IS ILLEGAL**

### Legal Restrictions:
- ✗ Do NOT use this tool on systems you don't own
- ✗ Do NOT monitor other people's keyboards without explicit written permission
- ✗ Do NOT use to capture passwords, personal information, or sensitive data
- ✗ Unauthorized keylogging violates:
  - Computer Fraud and Abuse Act (CFAA) in the US
  - Computer Misuse Act in the UK
  - Similar laws in virtually all countries
  - Privacy laws and regulations (GDPR, CCPA, etc.)

### Penalties for Unauthorized Use:
- Federal criminal charges
- Civil lawsuits
- Imprisonment (up to 10 years in some jurisdictions)
- Substantial fines ($10,000+)
- Restitution to victims

### ONLY Use This For:
- ✓ Your own personal computer/system
- ✓ Authorized penetration testing with written permission
- ✓ Security research in controlled lab environments
- ✓ Educational learning only
- ✓ Professional cybersecurity work with explicit authorization

**If you use this tool for unauthorized purposes, you assume all legal liability and consequences.**

## Ethical Considerations

- Always obtain proper authorization before deploying monitoring tools
- Be transparent about security research and testing activities
- Follow responsible disclosure practices
- Respect user privacy and data protection regulations
- Use security knowledge to protect systems, not harm them
- Consider the ethical implications of monitoring technology

## Security Implications

This project demonstrates:
- How keystroke capture works at the OS level
- How Python's logging module can be used for event tracking
- Why users should disable unknown background processes
- The importance of endpoint protection
- Why antivirus/EDR tools flag keystroke monitors
- How attackers establish persistence on systems
- The risk of sensitive data exposure (passwords, credit cards, etc.)

## Educational Value

By studying this code, you'll learn:
- Event-driven programming with keyboard listeners
- Python class architecture and design patterns
- File I/O and logging best practices
- Menu-driven user interfaces
- Cross-platform Python development
- Security research methodologies
- System-level input monitoring techniques

## Files Generated

When running:
- `keylog.txt` - Log file containing all captured keystrokes with timestamps

### This project was developed as part of a cybersecurity learning initiative to understand encryption fundamentals and secure file protection methods.

### This project is not intended to be used maliciously. If you do that, shame on you. >:(

---

**Remember:** With great power comes great responsibility. Use this knowledge ethically and legally.
