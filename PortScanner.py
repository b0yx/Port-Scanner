import pyfiglet
import sys
import socket
from datetime import datetime

# Displaying ASCII banner
ascii_banner = pyfiglet.figlet_format("Khalid alabsi")
print(ascii_banner)

# Check if exactly one argument is passed
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Resolve the hostname to an IP address
else:
    print("Invalid amount of Arguments")
    sys.exit()  # Exit the program if the argument is not valid

print("-" * 80)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 80)

# Try block to catch errors and handle the scanning process
try:
    for port in range(1, 65535):  # Scanning all ports from 1 to 65534
        print(f"Scanning port: {port}")
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  # Create a TCP socket
        socket.setdefaulttimeout(1)  # Set a timeout of 1 second per connection attempt
    
        result = s.connect_ex((target, port))  # Attempt to connect to the target on the current port
        if result == 0:  # If the result is 0, the port is open
            print(f"Port {port} is open")
        s.close()  # Close the socket after checking the port
    
except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()  # Exit the program if interrupted by the user

except socket.gaierror:
    print("\nHostname could not be resolved !!!!")
    sys.exit()  # Exit if the hostname cannot be resolved

except socket.error:
    print("\nServer not responding !!!!")
    sys.exit()  # Exit if there is a socket-related error
