def expense_tracker():
    expenses = []  # List to store expense dictionaries

    print("--- Welcome to the Professional Expense Tracker ---")

    while True:
        print("\nMain Menu:")
        print("1. ➕ Add an Expense")
        print("2. 📋 View All Expenses")
        print("3. 💰 View Total Spending")
        print("4. 🚪 Exit")

        choice = input("\nSelect an option (1-4): ")

        # 1. Adding an Expense
        if choice == "1":
            try:
                name = input("What did you buy? (e.g., Food, Travel, Clothes): ").strip()
                
                # Validation: Ensure amount is a number
                amount = float(input("Enter the amount spent: ₹"))
                
                date = input("Enter date (YYYY-MM-DD) [Leave blank for Today]: ").strip()
                if not date:
                    import datetime
                    date = datetime.date.today().strftime("%Y-%m-%d")
                
                category = input("Enter a brief description/category: ").strip()

                expense = {
                    "name": name,
                    "amount": amount,
                    "date": date,
                    "category": category
                }

                expenses.append(expense)
                print(f"\n✅ Success: Added ₹{amount} for {name}.")
            except ValueError:
                print("\n❌ Error: Please enter a valid number for the amount.")

        # 2. Viewing Expenses
        elif choice == "2":
            if not expenses:
                print("\nEmpty: No expenses recorded yet.")
            else:
                print(f"\n{'Date':<12} | {'Item':<15} | {'Amount':<10} | {'Category'}")
                print("-" * 55)
                for exp in expenses:
                    print(f"{exp['date']:<12} | {exp['name']:<15} | ₹{exp['amount']:<9} | {exp['category']}")

        # 3. Viewing Total
        elif choice == "3":
            total = sum(exp["amount"] for exp in expenses)
            print(f"\n📊 Total Expenditure: ₹{total:,.2f}")

        # 4. Exit
        elif choice == "4":
            print("\nExiting... Thank you for using the Expense Tracker!")
            break

        else:
            print("\n⚠️ Invalid selection. Please choose between 1 and 4.")

if __name__ == "__main__":
    expense_tracker()
