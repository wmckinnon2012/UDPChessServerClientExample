import socket

def udp_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address and port
    server_address = ('192.168.1.17', 12345)  # Change to match the server's IP and port

    try:
        # Send data to the server
        message = "C7D8"
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Receive the response from the server
        data, server_address = client_socket.recvfrom(1024)
        print(f"Received response from {server_address}: {data.decode('utf-8')}")

    finally:
        # Close the socket when done
        client_socket.close()

if __name__ == "__main__":
    udp_client()
