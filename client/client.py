import socket
import struct

def send_data(integer, boolean):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.12.9', 12345))

    # Pack the integer and boolean into a bytes object
    data = struct.pack('Ib', integer, boolean)
    client_socket.sendall(data)

    client_socket.close()

if __name__ == "__main__":
    send_data(4, True)  # Example: sending integer 42 and boolean True
