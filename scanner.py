import sys
import socket
import threading
import time

#to display date and time in this format
time_format_string = "{}/{}/{} {}:{}:{}".format("%d","%m","%y","%H","%M","%S")

#for open ports
open_ports = []

# Port scanner function
def scan_port(target, port, verbose):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print("Port {} is open".format(port))
    elif verbose:
        print("Port {} is closed".format(port))
    
    s.close()

# Define main function
def main():
    if len(sys.argv) == 4:
        try:
            # Get target IP address
            target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
            
            # Get port range
            port_range = sys.argv[2].split('-')
            start_port = int(port_range[0])
            end_port = int(port_range[1])
            
            # Verbose flag
            verbose = sys.argv[3].lower() == 'true'
            
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                raise ValueError("Port range is out of bounds or invalid.")
            
        except socket.gaierror:
            print("Hostname could not be resolved.")
            sys.exit()

        except ValueError as e:
            print("Ensure the port range is specified as 'startPort-endPort' with numeric values between 0 and 65535.")
            sys.exit()
        
    else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py <target> <startPort-endPort> <verbose: True/False>")
        sys.exit()

    # Add a banner
    print("-" * 50)
    print("Scanning target {}".format(target))
    print("Port range: {}-{}".format(start_port, end_port))
    print("Time started:",time.strftime(time_format_string))
    print("-" * 50)

    # Start scanning ports using threads
    try:
        threads = []
        start_time = time.time()

        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target, port, verbose))
            threads.append(t)
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()

        end_time = time.time()
        print("="*50)
        print("Open ports found are:", open_ports)
        print("="*50)
        print("Total time taken (in seconds):", (end_time - start_time))

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
        
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

main()
