import socket
import time

print("=" * 40)
print("      Python Port Scanner V2")
print("=" * 40)

target = input("Enter Target IP/Hostname: ")

ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

open_ports = []

start_time = time.time()

print("\nScanning", target, "...\n")

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
     try:
        service = socket.getservbyport(port)
     except:
        service = "Unknown"

    print(f"[+] Port {port} ({service.upper()}) is OPEN")
    open_ports.append(port)

    s.close()

end_time = time.time()

print("\n" + "=" * 40)
print("Scan Complete")
print("=" * 40)

print("Open Ports Found:", len(open_ports))

if open_ports:
    print("Open Ports:", open_ports)
else:
    print("No open ports found.")

print(f"Time Taken: {end_time - start_time:.2f} seconds")