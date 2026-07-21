"""
Day 5 Mini Project

Cybersecurity Host Checker

Author: Finn Tran
"""

print("===== Cybersecurity Host Checker =====")

def get_host():
    return input("Enter hostname: ")

def scan(host):
    print ("Checking host...")
    print (f"Target: {host}")
    print ("Scan completed.")

host = get_host()
if host == "":
    print("Hostname cannot be empty.")
else:    
    scan(host)
