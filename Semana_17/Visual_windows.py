import FreeSimpleGUI as sg
import json
from CSV_data_manager import download_report, load_report

class Categories:
    FILE_NAME = "categories.json"

    @staticmethod
    def save(categories):
        with open(Categories.FILE_NAME, "w") as file:
            json.dump(categories, file)

    @staticmethod
    def load():
        try:
            with open(Categories.FILE_NAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def __init__(self):
        self.categories = Categories.load()

        self.layout = [
            [sg.Text("Category Manager")],
            [sg.Listbox(self.categories, size=(30, 5), key="-CATEGORY_LIST-", enable_events=True)],
            [sg.Input(key="-NEW_CATEGORY-"), sg.Button("Add Category")],
            [sg.Button("Save & Exit")]
        ]
        self.window = sg.Window("Categories", self.layout)

    def run(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Save & Exit"):
                Categories.save(self.categories)  
                break

            elif event == "Add Category":
                new_category = values["-NEW_CATEGORY-"].strip()

                if new_category and new_category not in self.categories:
                    self.categories.append(new_category)
                    self.window["-CATEGORY_LIST-"].update(self.categories)

        self.window.close()


class Transaction_manager:

    FILE_NAME = "Transaction.json"

    @staticmethod
    def save_transaction_data(data):
        with open("Transaction.json", "w") as file:
            json.dump(data, file)


    @staticmethod
    def load_transaction_data():
        try:
            with open("Transaction.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        

    @staticmethod
    def positive_number(amount):
        try:
            amount= float(amount)
            return amount >=0
        except ValueError:
            return False
    
    
    @staticmethod
    def description_not_empty(description):
        try:
            description != "" 
            return description
        except SyntaxError:
            return False


    def __init__(self):
        self.categories = Categories.load()
        self.transaction_type= ["Expense", "Income"]
        self.amount = Transaction_manager.positive_number
        

        self.layout = [
            [sg.Text("transaction Tracker")],
            [sg.Text("Type of Transaction"), sg.Combo(self.transaction_type, key="-TRANSACTION_TYPE-", size=(20, 3))],
            [sg.Text("Description"), sg.Input(key="-DESCRIPTION-")],
            [sg.Text("Category"), sg.Combo(self.categories, key="-CATEGORY-", size=(20, 3))],
            [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
            [sg.Button("Save"), sg.Button("Cancel")]
        ]
        self.window = sg.Window("Transaction", self.layout)
    
    def run(self):

        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            elif event == "Save":
                transaction_type = values["-TRANSACTION_TYPE-"]
                category = values["-CATEGORY-"]
                description = values["-DESCRIPTION-"].strip()
                amount = values["-AMOUNT-"].strip()

                if not Transaction_manager.description_not_empty(description):
                    sg.popup_error("The Description must be fill")
                    continue

                if not Transaction_manager.positive_number(amount):
                    sg.popup_error("The Amount must be positive")
                    continue

                if transaction_type and category and description and self.amount:
                    data = Transaction_manager.load_transaction_data()
                    data.append({"type": transaction_type, "category": category, "description": description, "amount": float(amount)})
                    Transaction_manager.save_transaction_data(data)
                    sg.popup(f"{transaction_type} saved successfully")
                    break
                else:
                    sg.popup("Please fill in all fields")

        self.window.close()


class Show_current_transactions:
    
    def __init__(self):
        self.data= [list(transaction.values()) for transaction in Transaction_manager.load_transaction_data()]
        self.headings = ["Type", "Category", "Description","Amount"]
        self.layout = [
            [sg.Text("Current Transactions")],
            [sg.Table(values=self.data, headings= self.headings,auto_size_columns= False, justification= "Center" , enable_events= True,num_rows= 10, key="-TRANSACTION_LIST-", )],
            [sg.Button("Back")]
        ]

        self.window = sg.Window("Transactions", self.layout)

    def run(self):
        
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Back"):
                break

        self.window.close()


class Show_report:
    
    def __init__(self):
        
        self.layout = [
            [sg.Text("Report")],
            [sg.Button("Download Report"), sg.Button("Load Report")],
            [sg.Button("Back")]
        ]

        self.window = sg.Window("Report", self.layout)

    
    def run(self):
        while True:
            event, _ = self.window.read()

            if event in (sg.WIN_CLOSED, "Back"):
                break

            elif event == "Download Report":
                download_report()

            elif event == "Load Report":
                load_report()

        self.window.close()