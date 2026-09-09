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
    print("Preview only — this fault has not been saved.")

def main():
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