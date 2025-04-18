import time
import random

# Global variables
registered_users = []

# Validate username (non-empty, no special characters)
def is_valid_username(username):
    return username.isalnum() and username != ""

# Register a new user
def register_user():
    username = input("Enter a unique username: ").strip()
    if not is_valid_username(username):
        print("Invalid username. Only letters and numbers are allowed.")
    elif username in registered_users:
        print("Username already registered.")
    else:
        registered_users.append(username)
        print(f"Registered successfully! Total users: {len(registered_users)}")

# Pick and display a winner
def pick_winner():
    winner = random.choice(registered_users)
    print("\n******** Lottery Result ********")
    print(f"Winner: {winner}")
    print(f"Total participants: {len(registered_users)}")
    print("********************************")

# Main program
def main():
    print("🎉 Welcome to the Lottery System! 🎉")
    try:
        max_users = int(input("Enter the number of users to register: "))
        if max_users <= 0:
            print("Number of users must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    registration_duration = 300  # 5 minutes in seconds
    start_time = time.time()

    while len(registered_users) < max_users:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= registration_duration:
            print("\n⏰ Registration time is over!")
            break

        register_user()

    if len(registered_users) == 0:
        print("No users registered. Exiting program.")
        return

    pick_winner()

if __name__ == "__main__":
    main()
