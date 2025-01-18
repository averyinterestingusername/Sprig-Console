import socket
import pydirectinput
import credentials

# Constants for configuration
SERVER_HOST = credentials.SERVER_HOST
SERVER_PORT = credentials.SERVER_PORT
BUFFER_SIZE = 1024

def udp_server(host=SERVER_HOST, port=SERVER_PORT):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Set socket options for ultra-low latency
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 0)  # Minimize receive buffer
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 0)  # Minimize send buffer
        server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255)  # Maximize TTL to avoid network delays
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow address reuse

        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # print(f"Server listening on {host}:{port}...")
        print(f"Server listening on port {port}...")

        while True:
            try:
                data, addr = server_socket.recvfrom(BUFFER_SIZE)  # Receive packet
                if data:
                    # print(f"Received packet from {addr}: {data}")
                    key = data.decode('utf-8')
                    if key[1] == 'p':
                        pydirectinput.keyDown(key[0])
                    else:
                        pydirectinput.keyUp(key[0])
                else:
                    print(f"Received empty packet from {addr}")
            except KeyboardInterrupt:
                print("Server terminated.")
                break
            except Exception as e:
                print(f"Error receiving data: {e}")

    finally:
        # Cleanup socket
        server_socket.close()


if __name__ == "__main__":
    udp_server()

# # # 
