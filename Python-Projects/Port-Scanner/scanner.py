import socket
host = input("Enter host: ")
ports = [22, 80, 443]
for port in ports:
    client = socket.socket()
    client.settimeout(2)
    try:
        result = client.connect_ex((host,port))
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
    except:
        print("Host not found.")
        break
    client.close()
