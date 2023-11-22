import threading
import user_interactions
import dashboard


def update_status(user_id, status):
    user_interactions.update_status(user_id, status)
    print(f"Updated status for user {user_id} to {status}")


def user_panel():
    user_interactions.user_panel()


if __name__ == "__main__":
    print("Welcome to the Application!")

    user_panel_thread = threading.Thread(target=user_panel)
    dashboard_thread = threading.Thread(
        target=dashboard.show_real_time_analytics)

    user_panel_thread.start()
    dashboard_thread.start()

    user_panel_thread.join()
    dashboard_thread.join()

    print("Exiting the Application!")
