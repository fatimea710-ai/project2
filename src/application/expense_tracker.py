
from src.persistence.file_persister import FilePersister


class ExpenseTracker:

    def __init__(self):
        self._expenses = []
        self._file_persister = FilePersister()

    def add_expense(self, date, category, amount, description):
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        self._expenses.append(expense)

    def display_expenses(self):
        for expense in self._expenses:
            print(expense)

    def filter_by_category(self, category):
        for expense in self._expenses:
            if expense["category"].lower() == category.lower():
                print(expense)

    def filter_by_date(self, start_date, end_date):
        for expense in self._expenses:
            if start_date <= expense["date"] <= end_date:
                print(expense)

    def save_expenses(self, filename):
        self._file_persister.save_expenses(self._expenses, filename)

    def load_expenses(self, filename):
        self._expenses = self._file_persister.load_expenses(filename)

    def export_expenses(self, filename):
        self._file_persister.export_to_csv(self._expenses, filename)
