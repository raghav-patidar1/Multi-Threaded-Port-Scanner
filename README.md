# Multi-threaded Port Scanner in Python

This is a Python-based multi-threaded port scanner designed to scan ports on a target host efficiently. It supports three types of scanning: range-based, specific multi-port scanning, and single port scanning. The tool uses Python's `socket` and `threading` libraries to provide fast and customizable scanning options.

## Features

- **Range-Based Port Scanning**: Scan a range of ports (e.g., 80-550).
- **Specific Multi-Port Scanning**: Scan multiple specific ports (e.g., 80, 443, 3306).
- **Single Port Scanning**: Scan a single port (e.g., 80).
- **Multi-threaded for Efficiency**: Uses threads to scan multiple ports simultaneously, reducing scan time.
- **Verbose Mode**: Option to see both open and closed ports.
- **Robust Error Handling**: Handles invalid input, hostname resolution errors, and connection issues.

## Requirements

- Python 3.x

No additional external libraries are required.

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/raghav-patidar1/Multi-Threaded-Port-Scanner.git

cd Multi-Threaded-Port-Scanner
```

### 2. Run the scanner with the following syntax:

```bash
python3 scanner.py <target> <port-range/multi-port/single-port> <verbose: true/false>
```

- `<target>`: The IP address or domain name of the target.
- `<port-range/multi-port/single-port>`: Specify the ports to scan.
  
  - Example for range-based scanning: 80-550
  - Example for multi-port scanning: 80,443,3306
  - Example for single-port scanning: 80
    
- `<verbose>`: true or false (whether to show closed ports or not).

### 3. Example Commands:

- **Range-Based Port Scanning:**
  
   ```bash
   python3 scanner.py localhost 80-100 true

  ```

  Scans ports 80 to 100 on `localhost` and shows both open and closed ports.

- **Specific Multi-Port Scanning:**

  ```bash
  python3 scanner.py localhost 22,80,443 true
  
  ```

  Scans ports 22, 80, and 443 on `localhost`

- **Single Port Scanning:**
  
   ```bash
   python3 scanner.py localhost 80 false

  ```

  Scans port 80 on `localhost` and only shows open ports.

## Error Handling

- **Invalid Port Range**: Ensures ports are in the range of 0-65535.
- **Invalid Hostname**: Catches errors if the target hostname can't be resolved.
- **Invalid Input**: Proper validation of input formats for ranges, multi-port lists, and single ports.
- **Connection Errors**: Handles issues where the server can't be reached.

## How It Works

- The script first resolves the target domain to an IP address.
- Depending on the input type, it then scans a range of ports, multiple specific ports, or a single port.
- Multi-threading is used to scan ports simultaneously, speeding up the process.
- You can choose to enable verbose mode to view closed ports or limit the output to only open ports.

## Contributing

Feel free to open issues or submit pull requests to improve the project.



