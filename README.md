# Port Scanner

This is a simple port scanner built using Python that scans a given host for open ports. The script resolves a given hostname to an IP address and checks all ports from 1 to 65535 to identify open ports.

---

## Features

- Resolves a hostname to an IP address using `socket.gethostbyname()`.
- Scans ports from 1 to 65535 to check if they are open.
- Displays a banner with ASCII art of the author's name.
- Handles common exceptions such as invalid hostnames, connection errors, and keyboard interruptions.
- Displays the time when the scan started.

---

## Prerequisites

- Python 3.x (recommended).
- `pyfiglet` module for ASCII art (can be installed via `pip`).

---

## Installation

### 1. Clone this repository
You can clone this repository using the following command:

'git clone https://github.com/your-username/port-scanner.git'

## How to Run

To use this script, you need to provide the target hostname or IP address you want to scan as an argument.

### Command:

'python port_scanner.py target-IP'

