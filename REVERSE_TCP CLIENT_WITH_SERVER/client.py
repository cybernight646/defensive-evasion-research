import socket

server_ip = "127.0.0.1"   # Change to server address if remote
server_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((server_ip, server_port))
    print(f"[*] Connected to {server_ip}:{server_port}")

    message = b"Hello from client"
    client.sendall(message)
    print(f"[*] Sent: {message!r}")

    response = client.recv(1024)
    print(f"[*] Received: {response!r}")

except Exception as e:
    print(f"[!] Connection error: {e}")

finally:
    client.close()
    print("[*] Connection closed")
