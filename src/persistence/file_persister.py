
import json


class FilePersister:

    def save_expenses(self, expenses, filename):
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=4)

    def load_expenses(self, filename):
        with open(filename, "r") as file:
            expenses = json.load(file)
        return expenses
