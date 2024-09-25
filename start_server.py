import socket
import struct

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.12.9', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive the data
    data = conn.recv(5)  # 4 bytes for int + 1 byte for bool
    if len(data) == 5:
        integer, boolean = struct.unpack('Ib', data)
        print(f"Received integer: {integer}, boolean: {boolean}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
