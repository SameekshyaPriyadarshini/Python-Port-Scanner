import socket

print("Program Started")

target = "google.com"
port = 80

print("Creating Socket...")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket Created")

s.settimeout(5)

print("Trying to connect...")

result = s.connect_ex((target, port))

print("Result =", result)

if result == 0:
    print(" Port is Open")
else:
    print(" Port is Closed")

s.close()

print("Program Finished")