import socket


def login(username, password):
    # Placeholder for login logic
    print(f"User {username} logged in")


def register(username, password):
    # Placeholder for registration logic
    print(f"User {username} registered")


def delete_account(username):
    # Placeholder for account deletion logic
    print(f"User {username} account deleted")


def update_user(username):
    # Placeholder for user update logic
    print(f"User {username} updated")


def monitor_database():
    # Placeholder for database monitoring logic
    print("Admin monitoring database")


def handle_client_message(message):
    parts = message.split(':')
    if len(parts) >= 2:
        action = parts[0]
        if action == 'LOGIN' and len(parts) == 3:
            username, password = parts[1:]
            login(username, password)
        elif action == 'REGISTER' and len(parts) == 3:
            username, password = parts[1:]
            register(username, password)
        elif action == 'DELETE' and len(parts) == 2:
            username = parts[1]
            delete_account(username)
        elif action == 'UPDATE' and len(parts) == 2:
            username = parts[1]
            update_user(username)
        elif action == 'MONITOR':
            monitor_database()
        else:
            print("Invalid message format")
    else:
        print("Invalid message format")


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
        handle_client_message(message)


if __name__ == "__main__":
    udp_server()
