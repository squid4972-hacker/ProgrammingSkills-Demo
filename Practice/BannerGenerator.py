"""

Author: Enaya S. Laborn
Date: 29 August 2026
This program creates a standardized script that generates an official Session Metadata
& Operator Banner whenever a user logs in to perform routine administrative work.
The program will prompt the user for: Operator Name, Department Name, Workstation/Server ID,
and Estimated system uptime in hours.

"""

operatorName = input("Please enter the operator's name: ")
deptName = input("Please enter the department's name: ")
serverNum = input("Please enter the Workstation/Server ID's number: ")
uptime = input("Please enter the uptime(in hours): ")
uptimeDays = int(uptime) / 24  #Calculate uptime in days by dividing the uptime in hours by 24

print(f"""{'#' * 50} 
Operator Name: {operatorName}
Department: {deptName}
Workstation/Server ID: {serverNum}
Uptime (in days): {uptimeDays} days
{'#' * 50}""")
