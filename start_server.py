
from RPLCD.i2c import CharLCD

import socket
import struct
import gpiozero
import time

# init LCD screen
lcd = CharLCD('PCF8574', 0x27)

#lcd.cursor_pos = (1, 0)  # Move to the second row, first column


pinOuts = [17, 27, 22, 10, 9, 11, 20, 16, 26]

# Create a list of relay devices
relays = [gpiozero.OutputDevice(pin, active_high=False, initial_value=False) for pin in pinOuts]

def lcd_display(row, text):

    lcd.cursor_pos = (row, 0)
    lcd.write_string(text)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.12.9', 12345))
    server_socket.listen(5)  # Listen for up to 5 connections
    print("Server is listening on port 12345")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        lcd_display(0, "connection:")
        lcd_display(1, str(addr))
        time.sleep(2)
        lcd.clear()

        try:
            while True:
                data = conn.recv(5)  # 4 bytes for int + 1 byte for bool
                if not data:
                    break  # Break the inner loop if no data is received
                if len(data) == 5:
                    integer, boolean = struct.unpack('Ib', data)
                    print(f"Received integer: {integer}, boolean: {boolean}")
                    
                    # Ensure the integer is within the correct range
                    if 1 <= integer <= len(relays):
                        relay = relays[integer - 1]  # Get the corresponding relay (1-based index)
                        if boolean:
                            print(f"Setting relay{integer} ON")
                            relay.on()
                        else:
                            print(f"Setting relay{integer} OFF")
                            relay.off()
                    else:
                        print(f"Invalid relay number: {integer}")
                else:
                    print("Received malformed data")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()  # Close the connection

if __name__ == "__main__":
    start_server()
