import socket
import struct

import sys
import time
import gpiozero

pinOuts = [2, 3, 4, 17, 27, 22, 10, 9, 11, 0, 5, 6]

global relay1, relay2, relay3, relay4, relay5, relay6, relay7, relay8, relay9, relay10, relay11, relay12

relay1 = gpiozero.OutputDevice(pinOuts[0], active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(pinOuts[1], active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(pinOuts[2], active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(pinOuts[3], active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(pinOuts[4], active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(pinOuts[5], active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(pinOuts[6], active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(pinOuts[7], active_high=False, initial_value=False)
relay9 = gpiozero.OutputDevice(pinOuts[8], active_high=False, initial_value=False)
relay10 = gpiozero.OutputDevice(pinOuts[9], active_high=False, initial_value=False)
relay11 = gpiozero.OutputDevice(pinOuts[10], active_high=False, initial_value=False)
relay12 = gpiozero.OutputDevice(pinOuts[11], active_high=False, initial_value=False)

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
                    relay = "relay"+str(integer)
                    if bool(boolean):
                        print(f"Setting relay{integer} ON")
                        relay.on()
                    else:
                        print(f"Setting relay{integer} OFF")
                        relay.off()
                else:
                    print("Received malformed data")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()  # Close the connection

if __name__ == "__main__":
    start_server()
