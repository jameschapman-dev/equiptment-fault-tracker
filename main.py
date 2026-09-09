def main():
    while True:
        print("\nEquipment Fault Tracker")
        print("1. Report a fault")
        print("2. View faults")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Fault reporting is coming next.")
        elif choice == "2":
            print("Fault viewing is coming next.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()