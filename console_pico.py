import socket
import time
import network
from machine import Pin
import credentials

# Constants for configuration
SERVER_HOST = credentials.SERVER_HOST
SERVER_PORT = credentials.SERVER_PORT
BUFFER_SIZE = 1024
TIMEOUT = 1  # seconds for select timeout

# Wi-Fi credentials
SSID = credentials.SSID
PASSWORD = credentials.PASSWORD

# Set up button pin
button_pins = {5: 'w', 6: 'a', 7: 's', 8: 'd', 12: 'i', 13: 'j', 14: 'k', 15: 'l'}
button_map = {}

# Set up buttons
for pin in button_pins:
    button = Pin(pin, Pin.IN, Pin.PULL_UP)
    button_map[button] = {'char': button_pins[pin], 'pressed': False}

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        pass
    
    print(wlan.ifconfig())
    Pin('LED', Pin.OUT).value(1)

def send_keypress(key, client_socket, server_host=SERVER_HOST, server_port=SERVER_PORT):
    if key['pressed']:
        message = key['char'] + 'p'
    elif not key['pressed']:
        message = key['char'] + 'n'

    client_socket.sendto(message, (server_host, server_port))

def udp_client(server_host=SERVER_HOST, server_port=SERVER_PORT):
    # Initialize Wi-Fi connection
    connect_wifi()

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Set socket options for ultra-low latency
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 0)  # Minimize receive buffer
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 0)  # Minimize send buffer
        client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255)  # Maximize TTL to avoid network delays

        # Disable Nagle's algorithm (TCP_NODELAY)
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        # Set socket to non-blocking mode
        client_socket.setblocking(0)

        print(f"Sending messages to {server_host}:{server_port}...")

        while True:
            try:
                # Send message to the server
                for button in button_map:
                    if not button.value():  # Button pressed
                        if not button_map[button]['pressed']:  # Check if it was not already pressed
                            button_map[button]['pressed'] = True  # Update the state to pressed
                            send_keypress(button_map[button], client_socket)
                    else:  # Button released
                        if button_map[button]['pressed']:  # Check if it was already pressed
                            button_map[button]['pressed'] = False  # Update the state to released
                            send_keypress(button_map[button], client_socket)
            except socket.error as e:
                # Handle error gracefully (e.g., if socket is temporarily unavailable)
                print(f"Socket error: {e}")
                time.sleep(0.1)  # Small delay in case of an error
            except KeyboardInterrupt:
                print("Client terminated.")
                break

    finally:
        # Cleanup socket
        client_socket.close()


if __name__ == "__main__":
    udp_client()

# # # 
