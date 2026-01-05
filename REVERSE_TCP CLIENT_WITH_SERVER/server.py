import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket, address):
    try:
        data = client_socket.recv(1024)
        if not data:
            return

        print(f"[*] Received from {address[0]}:{address[1]} -> {data!r}")
        client_socket.sendall(b"ACK!")
    except Exception as e:
        print(f"[!] Error handling client {address}: {e}")
    finally:
        client_socket.close()

while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    client_handler = threading.Thread(
        target=handle_client,
        args=(client_socket, addr),
        daemon=True
    )
    client_handler.start()
