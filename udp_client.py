import socket


def send_request(request):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(request.encode(), (UDP_IP, UDP_PORT))
    client_socket.close()


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Login")
        print("2. Register")
        print("3. Delete Account")
        print("4. Update User")
        print("5. Monitor Database")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            send_request(f"LOGIN:{username}:{password}")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            send_request(f"REGISTER:{username}:{password}")
        elif choice == '3':
            username = input("Enter username: ")
            send_request(f"DELETE:{username}")
        elif choice == '4':
            username = input("Enter username: ")
            send_request(f"UPDATE:{username}")
        elif choice == '5':
            send_request("MONITOR")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
