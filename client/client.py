import socket
import struct
import time

def send_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.12.9', 12345))

    def test_all():
        print("\nPlease wait...\n")
        num = 1
        state = 1
        while num<=6:
            time.sleep(.5)
            data = struct.pack('Ib', num, state)
            client_socket.sendall(data)
            num+=1
        state = 0
        while num>=1:
            time.sleep(.5)
            data = struct.pack('Ib', num, state)
            client_socket.sendall(data)
            num-=1

    # Pack the integer and boolean into a bytes object
    connect = True
    while (connect):
        integer=input("exit/test/Relay number: ")
        if integer=="exit":
            connect = False
        if integer=="test":
            test_all()
        if connect:
            boolean=input("0 or 1: ")
            data = struct.pack('Ib', int(integer), int(boolean))

            client_socket.sendall(data)

    client_socket.close()

if __name__ == "__main__":
    send_data()  # Example: sending integer 42 and boolean True
