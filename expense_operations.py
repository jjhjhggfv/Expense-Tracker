def display_expenses(expenses):
    """Display all the expenses."""
    if not expenses:
        print("No expenses to show.")
        return

    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

def add_expense(expenses):
    """Add a new expense to the list."""
    category = input("Enter expense category: ")
    amount = input("Enter expense amount: ")
    date = input("Enter expense date (YYYY-MM-DD): ")
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added successfully!")
def delete_expense(expenses):
    """Delete an expense from the list."""
    if not expenses:
        print("No expenses to delete.")
        return

    display_expenses(expenses)  # Show the list of expenses
    try:
        index = int(input("Enter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            removed_expense = expenses.pop(index - 1)
            print(f"Deleted expense: {removed_expense['category']}, {removed_expense['amount']}, {removed_expense['date']}")
        else:
            print("Invalid number. No expense deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")
