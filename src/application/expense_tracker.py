
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
