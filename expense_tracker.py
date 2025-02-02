from expense_operations import display_expenses, add_expense, delete_expense

def main():
    # Greeting Messages
    print("*********************************************")
    print("🎉 Welcome to the Expense Tracker Application 🎉")
    print("Track your expenses easily and efficiently.")
    print("You can add, view, and delete your expenses.")
    print("*********************************************")

    expenses = []  # List to hold expenses in memory

    while True:
        print("\nExpense Tracker")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("\nThank you for using the Expense Tracker. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
