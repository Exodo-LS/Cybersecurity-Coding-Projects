# Log Analyzer
Welcome to my log analyzer project. The purpose of this project is to design a threat detection system in Python to gain a better understanding of how security operations centers (SOCs) analyze logs and identify malicious activity.

## How to use
### log_analyzer.py:
Before running, make sure you have Python 3.6+ installed. No external dependencies needed!

The program provides an interactive menu to analyze system logs for security threats using regex pattern matching and severity classification.

### Features:

* Scan logs for security threats

* Classify threats by severity (CRITICAL, WARNING, INFO)

* Detect authentication failures and brute force attempts

* Identify network reconnaissance (port scans)

* Find malware and exploit indicators

* Export findings to CSV for documentation

* Distinguish logs by filename

* Summary and detailed threat reporting

### Steps to use:

1. Run the program with python3 log_analyzer.py

2. Select option 1 to analyze a log file

3. Enter the path to your log file (e.g., test_system.log or /var/log/auth.log)

4. Optionally limit the number of lines to analyze

5. The program will scan for threats and display results

6. Use option 2 to view threat summary by severity

7. Use option 3 to view detailed threats with full information

8. Use option 4 to view critical threats only

9. Use option 5 to export all findings to CSV

### Threat Detection Patterns:

* CRITICAL: Failed password attempts, root access denied, SSH connection floods, shellcode, buffer overflows, exploits

* WARNING: Authentication failures, invalid users, sudo denied, port scans, segmentation faults, kernel errors

* INFO: Permission denied errors, file not found, normal connection closures

### Output Files:

* threats.csv - CSV export of all detected threats with logfile name, severity, and details

### Log File Formats Supported:

* Standard syslog format (MMM DD HH:MM:SS hostname service[pid]: message)

* Unstructured logs (with graceful fallback parsing)

* System logs from /var/log/auth.log, /var/log/syslog, etc.

Once finished, check the threat summary or export to CSV for detailed analysis and reporting.

### This project was developed as part of a cybersecurity learning initiative to understand log analysis, threat detection, and SOC operations.

### This project is not intended to be used maliciously. If you do that, shame on you. >:(
