from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socket
import struct

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f874fh74efujwedungufurwh3873w7857tgreufh8u7'  # Change this to a random secret key
socketio = SocketIO(app)

def get_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            # Connect to a public DNS server (this does not send data)
            sock.connect(("8.8.8.8", 80))
            local_ip = sock.getsockname()[0]
        except Exception as e:
            print(f"Error: {e}")
            return None
    return local_ip

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((get_ip(), 12345))

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    socketio.stop()

@app.route('/')
def index():
    return render_template('index.html')  # Make sure the HTML file is named index.html

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('response', 'Welcome to the WebSocket server!')

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('message')
def handle_message(message):
    print('Toggle:', message)
    data = struct.pack('Ib', int(message), int('1'))
    client_socket.sendall(data)
    emit('response', 'Message received: ' + message)  # Send a response back to the client

@socketio.on('location')
def handle_location(data):
    latitude = data['latitude']
    longitude = data['longitude']
    print(f"Received location - Latitude: {latitude}, Longitude: {longitude}")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=65432)
