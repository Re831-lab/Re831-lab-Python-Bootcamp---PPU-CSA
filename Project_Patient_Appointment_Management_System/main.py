from services import add_appointment, show_appointments, delete_appointment

def main_menu():
    while True:
        print("*** Appointment Management System ***")
        print("1. Add a new appointment")
        print("2. Show all appointments")
        print("3. Delete an appointment")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        print()
        if choice == "1":
            add_appointment()
        elif choice == "2":
            show_appointments()
        elif choice == "3":
            delete_appointment()
        elif choice == "4":
            print("Program terminated. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
