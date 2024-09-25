import socket
import struct

def send_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.12.9', 12345))

    # Pack the integer and boolean into a bytes object
    connect = True
    while (connect):
        integer=input("Relay number/exit: ")
        if integer=="exit":
            connect = False
        if connect:
            boolean=input("0 or 1: ")
            data = struct.pack('Ib', int(integer), int(boolean))

            client_socket.sendall(data)

    client_socket.close()

if __name__ == "__main__":
    send_data()  # Example: sending integer 42 and boolean True
