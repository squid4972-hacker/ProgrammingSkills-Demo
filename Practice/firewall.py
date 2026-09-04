"""
Author: Enaya L.
Date: 3 September 2026
This program creates a lightweight policy engine for a network gateway. The gateway receives incoming network packets containing an 
IP address, target port, and access request flag. Your script must process a batch of incoming requests and print an access verdict (ALLOW, DENY, or ALERT).

"""

# 1. Using provided list (structure is [Source IP, Target Port, Protocol])
requests = [
    ["192.168.1.50", 22, "TCP"],
    ["10.0.0.15", 80, "TCP"],
    ["203.0.113.5", 23, "TCP"],
    ["192.168.1.100", 443, "TCP"],
    ["198.51.100.77", 3389, "TCP"],
    ["198.168.100.77", 53, "UDP"]
]

# 2. Initialize the counter variables
inspected_ct = 0
allowed_ct = 0
denied_ct = 0
alerts_ct = 0

# 3. Loop, decide and print IP Address, destination port, protocol, and the verdict until the list ends
for sourceIP, port, protocol in requests:
    inspected_ct += 1
    
    if port == 23:
        print(f"[INSPECTING] {sourceIP}:{port} ({protocol}) -> VERDICT: DENY (Prohibited Protocol)")
        denied_ct += 1
    elif port == 3389 and not sourceIP.startswith(("192.168.", "10.")):
        print(f"[INSPECTING] {sourceIP}:{port} ({protocol}) -> VERDICT: ALERT (External RDP Request)")
        alerts_ct += 1
    elif port == 22 or port == 80 or port == 443:  # Allow pre-defined ports
        print(f"[INSPECTING] {sourceIP}:{port} ({protocol}) -> VERDICT: ALLOW")
        allowed_ct += 1
    else: 
        print(f"[INSPECTING] {sourceIP}:{port} ({protocol}) -> VERDICT: Contact Network Administrator") # Implementing implicit denials
        denied_ct += 1

# 4. Print summary of packets inspected
print(f"\nTotal Inspected: {inspected_ct}")
print(f"Total Allowed: {allowed_ct}")
print(f"Total Denied: {denied_ct}")
print(f"Total Alerts: {alerts_ct}")

