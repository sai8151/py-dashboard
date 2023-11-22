import time


def show_real_time_analytics(data):
    while True:
        print("\nDashboard - Real-Time Analytics")
        for user_id, user_data in data.items():
            status = user_data.get('status', 'Logged Out')
            print(f"User: {user_id}, Status: {status}")

        # Calculate and display other analytics (total interactions, purchases, etc.)
        # For the sake of simplicity, I'll omit these calculations for now.

        time.sleep(5)


if __name__ == "__main__":
    print("Welcome to Dashboard CLI!\n")

    users_data = {
        "user1": {"interactions": 0, "purchase_history": [], "status": "Logged Out"},
        "user2": {"interactions": 0, "purchase_history": [], "status": "Logged Out"}
    }

    show_real_time_analytics(users_data)
