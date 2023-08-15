import os
import time

def clear_terminal():
    os.system("clear" if os.name == "posix" else "cls")

def display_menu():
    clear_terminal()
    print("╔═══════════════════════╗")
    print("║ [STELLAR-WIZARD] [v1] ║")
    print("╠═══════════════════════╣")
    print("║ 1. Planet Finder      ║")
    print("║ 2. Positions          ║")
    print("║ 3. Events             ║")
    print("║ 4. Misc               ║")
    print("║ 5. README             ║")
    print("║ 6. Quit               ║")
    print("╚═══════════════════════╝")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice

def execute_script(script_name):
    clear_terminal()
    os.system(f"python3 {script_name}")
    input("Press Enter to continue...")

def main():
    # Display ASCII.txt for 2 seconds
    with open("ASCII.txt", "r") as ascii_file:
        ascii_art = ascii_file.read()
        print(ascii_art)
        time.sleep(2)
    
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            execute_script("planet_finder.py")
        elif choice == '2':
            execute_script("positions.py")
        elif choice == '3':
            execute_script("events.py")
        elif choice == '4':
            execute_script("misc.py")
        elif choice == '5':
            clear_terminal()
            os.system("cat README.md")
            input("Press Enter to continue...")
        elif choice == '6':
            clear_terminal()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
