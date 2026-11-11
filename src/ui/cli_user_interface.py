from src.application.expense_tracker import ExpenseTracker


class CLIUserInterface:

    def __init__(self):
        self._tracker = ExpenseTracker()

    def show_menu(self):
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an Expense")
        print("2. View the Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date Range")
        print("5. Save the Expenses")
        print("6. Load the Expenses")
        print("7. Export Expenses to CSV")
        print("8. Exit")

    def get_choice(self):
        choice = input("Enter your choice (1-8): ")
        return choice

    def add_expense(self):
        date = input("Enter expense date (YYYY-MM-DD): ")
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")

        self._tracker.add_expense(date, category, amount, description)

        print("Expense added successfully!")
    def view_expenses(self):
        print("\nYour Expenses:")
        self._tracker.display_expenses()

    def filter_by_category(self):
        category = input("Enter category to search: ")
        self._tracker.filter_by_category(category)
    def filter_by_date(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        self._tracker.filter_by_date(start_date, end_date)

    def save_expenses(self):
        filename = input("Enter filename to save expenses: ")
        self._tracker.save_expenses(filename)
        print("Expenses saved successfully!")

    def load_expenses(self):
        filename = input("Enter filename to load expenses: ")
        self._tracker.load_expenses(filename)
        print("Expenses loaded successfully!")

    def export_expenses(self):
        filename = input("Enter filename to export expenses: ")
        self._tracker.export_expenses(filename)
        print("Expenses exported successfully!")
        
    def run(self):
        while True:
            self.show_menu()
            choice = self.get_choice()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.filter_by_category()
            elif choice == "4":
                self.filter_by_date()
            elif choice == "5":
                self.save_expenses()
            elif choice == "6":
                self.load_expenses()
            elif choice == "7":
                self.export_expenses()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

     


