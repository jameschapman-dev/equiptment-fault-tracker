from database import initialise_database, save_fault
def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def report_fault():
    print("\nReport a fault")

    equipment = get_required_text("Equipment name: ")
    description = get_required_text("Describe the fault: ")

    while True:
        priority = input("Priority (low/medium/high): ").strip().lower()

        if priority in ("low", "medium", "high"):
            break

        print("Please enter low, medium or high.")

    print("\nFault details")
    print(f"Equipment: {equipment}")
    print(f"Description: {description}")
    print(f"Priority: {priority}")
    print("Status: open")
    fault_id = save_fault(equipment, description, priority)
    print(f"Fault #{fault_id} saved successfully.")

def main():
    initialise_database()
    while True:
        print("\nEquipment Fault Tracker")
        print("1. Report a fault")
        print("2. View faults")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            report_fault()
        elif choice == "2":
            print("Fault viewing is coming next.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()