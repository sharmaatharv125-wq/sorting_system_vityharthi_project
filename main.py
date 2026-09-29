expenses = []


def add_expense():
    print("\n--- ADD EXPENSE ---")

    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- ALL EXPENSES ---")

    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\nNo.  Name              Amount        Category")
        print("-" * 50)

        for i in range(len(expenses)):
            print(i + 1, "   ",
                  expenses[i]["name"],
                  "       ₹", expenses[i]["amount"],
                  "       ", expenses[i]["category"])


def total_expense():
    print("\n--- TOTAL EXPENSE ---")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total money spent: ₹", total)


def search_expense():
    print("\n--- SEARCH EXPENSE ---")

    search = input("Enter expense name: ")

    found = False

    for expense in expenses:
        if expense["name"].lower() == search.lower():
            print("\nExpense Found!")
            print("Name     :", expense["name"])
            print("Amount   : ₹", expense["amount"])
            print("Category :", expense["category"])
            found = True

    if found == False:
        print("Expense not found.")


def main():

    while True:

        print("\n")
        print("=" * 45)
        print("          💰 EXPENSE TRACKER")
        print("=" * 45)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Search Expense")
        print("5. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
