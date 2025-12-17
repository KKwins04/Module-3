def check_user_permission():
    # Simulate permission check
    return True

def check_critical_tasks():
    # Simulate check for running critical tasks
    return False  # False means no critical task is running

def check_system_state():
    # Simulate system health check
    return True

def confirm_shutdown():
    choice = input("Are you sure you want to shutdown? (Yes/No): ").lower()
    return choice == "yes"

def shutdown_system():
    print("System is shutting down safely...")

def main():
    if not check_user_permission():
        print("Shutdown denied: insufficient permissions.")
        return False

    if check_critical_tasks():
        print("Shutdown denied: critical tasks are running.")
        return True

    if not check_system_state():
        print("Shutdown denied: system state is unsafe.")
        return False

    if not confirm_shutdown():
        print("Shutdown cancelled by user.")
        return True

    shutdown_system()

if __name__ == "__main__":
    main()
