# UDP Client-Server Interaction System

This project demonstrates a basic UDP client-server interaction system for managing user actions and administrative tasks.

## Overview

The system consists of two components:

- `udp_server.py`: The UDP server that handles user and admin actions.
- `udp_client.py`: The UDP client that allows users to interact with the server by sending requests.

## Prerequisites

To run this project, ensure you have Python 3 installed on your system.

## How to Use

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/udp-client-server.git

  python3 user_manager.py
   ```

2. Run the UDP server:

   ```bash
   python3 server.py
   ```

3. Run the UDP client:

   ```bash
   python3 client.py
   ```

4. Choose from the available options to perform actions like login, register, delete account, update user, and monitor the database.

## Files Included

- `udp_server.py`: Contains the UDP server logic for handling client requests.
- `udp_client.py`: Provides a menu-driven interface for sending requests to the server.

## Usage Notes

- The server listens for UDP messages and executes actions based on the received requests from the client.
- Clients can perform various actions such as login, register, delete account, update user, and monitor the database by sending specific requests to the server.
- Customize the server logic in `udp_server.py` to implement actual functionality for handling user and admin actions.
- Modify the client-side prompts and actions in `udp_client.py` as needed for your application.
