import socket
import struct

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.12.9', 12345))
    server_socket.listen(5)  # Listen for up to 5 connections
    print("Server is listening on port 12345")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        try:
            while True:
                data = conn.recv(5)  # 4 bytes for int + 1 byte for bool
                if not data:
                    break  # Break the inner loop if no data is received
                if len(data) == 5:
                    integer, boolean = struct.unpack('Ib', data)
                    print(f"Received integer: {integer}, boolean: {boolean}")
                else:
                    print("Received malformed data")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()  # Close the connection

if __name__ == "__main__":
    start_server()
