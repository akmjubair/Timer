import time

# Function to display the modern timer clock
def display_timer(hours, minutes, seconds):
    print("\n--- Modern Timer Clock ---")
    print(f"  {hours:02}:{minutes:02}:{seconds:02}")
    print("-------------------------\n")

# Function to save timer details to a file
def save_to_file(data):
    with open("jubair_timer.txt", "a") as file:
        file.write(data + "\n")
    print(f"Data saved to 'jubair_timer.txt'.")

# Function to handle the countdown
def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = f'{hrs:02}:{mins:02}:{secs:02}'
        print(f"⏳ {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\n🎉 Time's up!")

# Menu options
def menu():
    print("\nMenu:")
    print("1. Add Timer")
    print("2. Show All Timers (Serial)")
    print("3. Remove Timer")
    print("4. Edit Timer")
    print("5. Search Timer")
    print("6. Exit")

# Main program
def main():
    timers = []  # List to store timer data
    while True:
        menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":  # Add Timer
            print("\n--- Add Timer ---")
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))
            display_timer(hours, minutes, seconds)
            timers.append((hours, minutes, seconds))
            save_to_file(f"Timer Added: {hours:02}:{minutes:02}:{seconds:02}")

        elif choice == "2":  # Show All Timers
            print("\n--- All Timers (Serial) ---")
            if not timers:
                print("No timers available.")
            else:
                for idx, (hours, minutes, seconds) in enumerate(timers, start=1):
                    print(f"{idx}. {hours:02}:{minutes:02}:{seconds:02}")

        elif choice == "3":  # Remove Timer
            print("\n--- Remove Timer ---")
            if not timers:
                print("No timers available to remove.")
            else:
                for idx, (hours, minutes, seconds) in enumerate(timers, start=1):
                    print(f"{idx}. {hours:02}:{minutes:02}:{seconds:02}")
                to_remove = int(input("Enter the serial number of the timer to remove: ")) - 1
                if 0 <= to_remove < len(timers):
                    removed_timer = timers.pop(to_remove)
                    print(f"Removed Timer: {removed_timer[0]:02}:{removed_timer[1]:02}:{removed_timer[2]:02}")
                    save_to_file(f"Timer Removed: {removed_timer[0]:02}:{removed_timer[1]:02}:{removed_timer[2]:02}")
                else:
                    print("Invalid serial number.")

        elif choice == "4":  # Edit Timer
            print("\n--- Edit Timer ---")
            if not timers:
                print("No timers available to edit.")
            else:
                for idx, (hours, minutes, seconds) in enumerate(timers, start=1):
                    print(f"{idx}. {hours:02}:{minutes:02}:{seconds:02}")
                to_edit = int(input("Enter the serial number of the timer to edit: ")) - 1
                if 0 <= to_edit < len(timers):
                    new_hours = int(input("Enter new hours: "))
                    new_minutes = int(input("Enter new minutes: "))
                    new_seconds = int(input("Enter new seconds: "))
                    timers[to_edit] = (new_hours, new_minutes, new_seconds)
                    print(f"Timer Updated to: {new_hours:02}:{new_minutes:02}:{new_seconds:02}")
                    save_to_file(f"Timer Edited: {new_hours:02}:{new_minutes:02}:{new_seconds:02}")
                else:
                    print("Invalid serial number.")

        elif choice == "5":  # Search Timer
            print("\n--- Search Timer ---")
            if not timers:
                print("No timers available to search.")
            else:
                search_hours = int(input("Enter hours to search: "))
                search_minutes = int(input("Enter minutes to search: "))
                search_seconds = int(input("Enter seconds to search: "))
                search_result = (search_hours, search_minutes, search_seconds)
                if search_result in timers:
                    print(f"Timer Found: {search_hours:02}:{search_minutes:02}:{search_seconds:02}")
                else:
                    print("Timer not found.")

        elif choice == "6":  # Exit
            print("\nExiting the program...")
            if timers:
                print("Starting countdown for the first timer.")
                countdown(*timers[0])  # Start countdown for the first timer in the list
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
