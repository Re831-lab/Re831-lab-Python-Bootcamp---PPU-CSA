from storage import appointments

def add_appointment():
    name = input("Enter patient name: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM AM/PM): ")
    appointment = {"name": name, "date": date, "time": time}
    appointments.append(appointment)
    print("Appointment added successfully.\n")


def show_appointments():
    if len(appointments) == 0:
        print("No appointments scheduled.\n")
        return
    
    print("\nAppointments list:")
    number = 1
    for app in appointments:
        print(str(number) + ". " + app["name"] + " - " + app["date"] + " - " + app["time"])
        number += 1
    print()


def delete_appointment():
    if len(appointments) == 0:
        print("No appointments to delete.\n")
        return
    
    show_appointments()
    choice = input("Enter the number of the appointment to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    idx = int(choice)

    if idx <= 0 or idx > len(appointments):
        print("Number out of range.\n")
    else:
        deleted = appointments[idx - 1]
        del appointments[idx - 1]
        print("Deleted appointment for " + deleted["name"] +
              " on " + deleted["date"] +
              " at " + deleted["time"] + ".\n")




