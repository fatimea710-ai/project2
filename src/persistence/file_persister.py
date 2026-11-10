
import json


class FilePersister:

    def save_expenses(self, expenses, filename):
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=4)
