import sys
import socket
import time
from threading import Thread

#to save all open ports on target
open_ports = list()

#to display time in this format
time_format_string = "{}/{}/{} {}:{}:{}".format("%d","%m","%y","%H","%M","%S")

# Port scanning function
def scan_port(target, port, verbose):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print(f"Port {port} is open")
    elif verbose:
        print(f"Port {port} is closed")

    s.close()

# Validate and process the port argument
def process_ports(port_arg):
    # Check for range-based port scanning (e.g., 80-550)
    if '-' in port_arg:
        start_port, end_port = port_arg.split('-')
        try:
            start_port = int(start_port)
            end_port = int(end_port)

            if start_port > end_port or not (0 < start_port <= 65535 and 0 < end_port <= 65535):
                raise ValueError
            return list(range(start_port, end_port + 1))
        except ValueError:
            raise ValueError("Invalid port range. Ensure it’s in the form startPort-endPort, with valid port numbers between 1 and 65535.")

    # Check for multi-port scanning (e.g., 80,443,3306)
    elif ',' in port_arg:
        ports = port_arg.split(',')
        try:
            return [int(port) for port in ports if 0 < int(port) <= 65535]
        except ValueError:
            raise ValueError("Invalid port numbers in the list. Ensure each port is a valid number between 1 and 65535.")

    # Single port scanning (e.g., 80)
    else:
        try:
            port = int(port_arg)
            if 0 < port <= 65535:
                return [port]
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Invalid single port. Ensure the port is a number between 1 and 65535.")

# Main function to start the port scanner
def main():
    if len(sys.argv) == 4:
        try:
            # Get target IP address
            target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4

            # Process the port argument (range, list, or single port)
            ports = process_ports(sys.argv[2])

            # Verbose flag (True/False)
            verbose = sys.argv[3].lower() == 'true'

        except socket.gaierror:
            print("Hostname could not be resolved.")
            sys.exit()

        except ValueError as e:
            print(f"Error: {e}")
            sys.exit()

    else:
        print("Invalid number of arguments.")
        print("Usage: python3 scanner.py <target> <port-range/multi-port/single-port> <verbose: true/false>")
        sys.exit()

    # Banner
    print("-" * 50)
    print("Scanning target {}".format(target))
    print(f"Ports: {', '.join(map(str, ports))}")
    print("Time started:",time.strftime(time_format_string))
    print("-" * 50)

    # Start scanning ports using threads
    try:
        threads = []
        start_time = time.time()

        for port in ports:
            t = Thread(target=scan_port, args=(target, port, verbose))
            threads.append(t)
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()
        
        end_time = time.time()

        print("="*50)
        print("Open ports found are:", open_ports)
        print("="*50)
        print("Total time taken (in seconds): {:.2f}".format((end_time - start_time)))

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.error:
        print("Could not connect to server.")
        sys.exit()

main()