import re
import os
from datetime import datetime
from collections import defaultdict
import csv


class ThreatLevel:
    """Threat severity levels"""
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class LogAnalyzer:
    def __init__(self):
        """Initialize analyzer with threat patterns"""
        
        self.current_logfile = "Unknown"

        # Threat patterns (regex: severity)
        self.threat_patterns = {
            # Authentication threats
            r"Failed password.*invalid user": ThreatLevel.CRITICAL,
            r"authentication failure": ThreatLevel.WARNING,
            r"Invalid user.*from": ThreatLevel.WARNING,
            r"root.*denied.*password": ThreatLevel.CRITICAL,
            r"sudo.*denied": ThreatLevel.WARNING,
            
            # Network threats
            r"port scan": ThreatLevel.WARNING,
            r"portscan": ThreatLevel.WARNING,
            r"SSH.*closed.*too many": ThreatLevel.CRITICAL,
            r"Connection closed by authenticating user": ThreatLevel.INFO,
            
            # System threats
            r"segmentation fault": ThreatLevel.WARNING,
            r"kernel.*error": ThreatLevel.WARNING,
            r"permission denied": ThreatLevel.INFO,
            r"file.*not found": ThreatLevel.INFO,
            
            # Malware/Exploit
            r"shellcode": ThreatLevel.CRITICAL,
            r"buffer overflow": ThreatLevel.CRITICAL,
            r"exploit": ThreatLevel.CRITICAL,
        }
        
        self.threats_found = []
        self.stats = defaultdict(int)
    
    def parse_syslog_line(self, line):
        """
        Parse a syslog line
        
        Returns:
            dict with timestamp, service, message
        """
        # Standard syslog format: MMM DD HH:MM:SS hostname service[pid]: message
        syslog_pattern = r"^(\w+ +\d+ \d+:\d+:\d+) (\S+) (.+?)(\[.+?\])?: (.*)$"
        
        match = re.match(syslog_pattern, line)
        if match:
            timestamp, hostname, service, pid, message = match.groups()
            return {
                'timestamp': timestamp,
                'hostname': hostname,
                'service': service,
                'pid': pid,
                'message': message
            }
        
        # Fallback for unstructured logs
        return {
            'timestamp': 'N/A',
            'hostname': 'N/A',
            'service': 'N/A',
            'pid': 'N/A',
            'message': line
        }
    
    def analyze_line(self, line):
        """
        Analyze a single log line for threats
        
        Args:
            line: Log line to analyze
        
        Returns:
            List of (threat_type, severity) tuples if threats found
        """
        threats = []
        
        # Check each threat pattern
        for pattern, severity in self.threat_patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                # Extract the matching pattern
                match = re.search(pattern, line, re.IGNORECASE)
                threat_type = match.group(0) if match else pattern
                
                threats.append({
                    'type': threat_type,
                    'severity': severity,
                    'line': line
                })
                
                # Update statistics
                self.stats[severity] += 1
        
        return threats
    
    def analyze_file(self, filepath, limit=None):
        """
        Analyze a log file
        
        Args:
            filepath: Path to log file
            limit: Maximum lines to analyze (None = all)
        """
        self.current_logfile = os.path.basename(filepath)
        print(f"Analyzing {filepath}...")
        
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            return False
        
        try:
            # Check if readable
            if not os.access(filepath, os.R_OK):
                print(f"Permission denied: {filepath}")
                print("Try running with sudo for /var/log files")
                return False
            
            line_count = 0
            
            with open(filepath, 'r', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    if limit and line_num > limit:
                        break
                    
                    line = line.strip()
                    if not line:
                        continue
                    
                    line_count += 1
                    
                    # Analyze line
                    threats = self.analyze_line(line)
                    if threats:
                        parsed = self.parse_syslog_line(line)
                        for threat in threats:
                            self.threats_found.append({
                                **threat,
                                **parsed,
                                'line_number': line_num,
                                'logfile': self.current_logfile
                            })
            
            print(f"Analysis complete: {line_count} log lines analyzed")
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def print_summary(self):
        """Print analysis summary"""
        print(f"\n{'='*60}")
        print(f"THREAT ANALYSIS SUMMARY")
        print(f"{'='*60}")
        
        if not self.threats_found:
            print("No threats detected!")
        else:
            print(f"Total threats detected: {len(self.threats_found)}\n")
            
            # Statistics by severity
            print("Threats by Severity:")
            for severity in [ThreatLevel.CRITICAL, ThreatLevel.WARNING, ThreatLevel.INFO]:
                count = self.stats[severity]
                if count > 0:
                    print(f"  {severity}: {count}")
        
        print(f"\n{'='*60}\n")
    
    def print_detailed_threats(self, show_critical_only=False):
        """Print detailed threat list"""
        if not self.threats_found:
            print("No threats to display")
            return
        
        # Filter if needed
        threats = self.threats_found
        if show_critical_only:
            threats = [t for t in threats if t['severity'] == ThreatLevel.CRITICAL]
        
        print(f"\n{'='*60}")
        print(f"DETAILED THREATS - {self.current_logfile} ")
        print(f"{'='*60}\n")
        
        for i, threat in enumerate(threats, 1):
            print(f"{i}. {threat['severity']} - From: {threat.get('logfile', 'Unknown')}")
            print(f"   Type: {threat['type']}")
            print(f"   Time: {threat['timestamp']}")
            print(f"   Host: {threat['hostname']}")
            print(f"   Service: {threat['service']}")
            print(f"   Line {threat['line_number']}: {threat['message'][:80]}")
            print()
    
    def export_threats_csv(self, filename="threats.csv"):
        """Export threats to CSV file"""
        
        if not self.threats_found:
            print("No threats to export")
            return
        
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'logfile', 'line_number', 'timestamp', 'hostname', 'service',
                    'severity', 'type', 'message'
                ])
                writer.writeheader()
                
                for threat in self.threats_found:
                    writer.writerow({
                        'logfile': threat.get('logfile', 'Unknown'),
                        'line_number': threat['line_number'],
                        'timestamp': threat['timestamp'],
                        'hostname': threat['hostname'],
                        'service': threat['service'],
                        'severity': threat['severity'],
                        'type': threat['type'],
                        'message': threat['line']
                    })
            
            print(f"Threats exported to {filename}")
        except Exception as e:
            print(f"Export failed: {e}")


def display_menu():
    """Display main menu"""
    print(f"\n{'='*60}")
    print("LOG ANALYZER")
    print(f"{'='*60}")
    print("1. Analyze a log file")
    print("2. View threat summary")
    print("3. View detailed threats")
    print("4. View critical threats only")
    print("5. Export threats to CSV")
    print("6. Exit")
    print(f"{'='*60}")
    return input("Select option (1-6): ")


def analyze_file_interactive(analyzer):
    """Interactive file analysis"""
    filepath = input("Enter log file path: ").strip()
    
    if not filepath:
        print("No file path entered")
        return
    
    limit_input = input("Max lines to analyze (press Enter for all): ").strip()
    limit = int(limit_input) if limit_input else None
    
    analyzer.analyze_file(filepath, limit)


def main():
    """Main program loop"""
    print(f"\n{'='*60}")
    print("LOG ANALYZER")
    print("Threat Detection in System Logs")
    print(f"{'='*60}\n")
    
    analyzer = LogAnalyzer()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            analyze_file_interactive(analyzer)
        elif choice == "2":
            analyzer.print_summary()
        elif choice == "3":
            analyzer.print_detailed_threats(show_critical_only=False)
        elif choice == "4":
            analyzer.print_detailed_threats(show_critical_only=True)
        elif choice == "5":
            filename = input("Enter CSV filename (default: threats.csv): ").strip()
            filename = filename if filename else "threats.csv"
            analyzer.export_threats_csv(filename)
        elif choice == "6":
            print("\nThank you for using Log Analyzer!")
            break
        else:
            print("Invalid option. Please try again.")


# Program entry point
if __name__ == "__main__":
    main()