# server.py
import socket
import user_manager as um


def handle_client_message(message, client_address, server_socket):
    parts = message.split(':')
    if len(parts) >= 2:
        action = parts[0]
        if action == 'LOGIN' and len(parts) == 3:
            username, password = parts[1:]
            if um.login(username, password):  # passes, id, pswd to login method in um module
                response = f"Login successful for user {username}"
            else:
                response = f"Invalid credentials for user {username}"
            server_socket.sendto(response.encode(), client_address)
        elif action == 'REGISTER' and len(parts) == 3:
            username, password = parts[1:]
            if um.register(username, password):
                response = f"User {username} registered successfully"
            else:
                response = f"User {username} already exists"
            server_socket.sendto(response.encode(), client_address)
        elif action == 'DELETE' and len(parts) == 2:
            username = parts[1]
            if um.delete_account(username):
                response = f"User {username} account deleted"
            else:
                response = f"User {username} not found"
            server_socket.sendto(response.encode(), client_address)
        elif action == 'UPDATE' and len(parts) == 2:
            username = parts[1]
            um.update_user(username)
            response = f"User {username} updated"
            server_socket.sendto(response.encode(), client_address)
        elif action == 'MONITOR':
            response = "Admin monitoring database"
            server_socket.sendto(response.encode(), client_address)
        else:
            response = "Invalid message format"
            server_socket.sendto(response.encode(), client_address)
    else:
        response = "Invalid message format"
        server_socket.sendto(response.encode(), client_address)


def udp_server():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((UDP_IP, UDP_PORT))

    print("UDP Server started...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received message: {message}")
        handle_client_message(message, addr, server_socket)


if __name__ == "__main__":
    udp_server()
