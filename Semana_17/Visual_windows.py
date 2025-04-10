import FreeSimpleGUI as sg
from Logic import Transaction, Category
from Data_manager import Save_categories_json, Save_transactions_json, Report
class Categories_window:

    def __init__(self):

        self.categories = Save_categories_json.load()
        self.layout = [
            [sg.Text("Category Manager")],
            [sg.Listbox(self.categories, size=(30, 5), key=Category().category, enable_events=True)],
            [sg.Input(key= Category().new_category), sg.Button("Add Category")],
            [sg.Button("Save & Exit")]
        ]
        self.window = sg.Window("Categories", self.layout)

    def run(self):
        from Data_manager import Save_categories_json
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Save & Exit"):
                Save_categories_json.save(self.categories)  
                break

            elif event == "Add Category":
                category_instance = Category()
                category_instance.add_new_category(values, self.categories, self.window)


        self.window.close()


class Transaction_manager_window:

    def __init__(self):
        self.categories = Save_categories_json.load()
        self.transaction_type= Transaction().transaction_type
        self.layout = [
            [sg.Text("transaction Tracker")],
            [sg.Text("Type of Transaction"), sg.Combo(self.transaction_type, key= Transaction().type, size=(20, 3))],
            [sg.Text("Description"), sg.Input(key=Transaction().description)],
            [sg.Text("Category"), sg.Combo(self.categories, key=Category().category, size=(20, 3))],
            [sg.Text("Amount"), sg.Input(key=Transaction().amount)],
            [sg.Button("Save"), sg.Button("Cancel")]
        ]
        self.window = sg.Window("Transaction", self.layout)
    
    def run(self):

        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            elif event == "Save":
                transaction_type = values[Transaction().type]
                category = values[Category().category]
                description = values[Transaction().description].strip()
                amount = values[Transaction().amount].strip()

                if not Transaction.description_not_empty(description):
                    sg.popup_error("The Description must be fill")
                    continue

                if not Transaction.positive_number(amount):
                    sg.popup_error("The Amount must be positive")
                    continue

                if transaction_type and category and description and amount:
                    Transaction.update_transaction(transaction_type, category, description, amount)
                    sg.popup(f"{transaction_type} saved successfully")
                    break
                else:
                    sg.popup("Please fill in all fields")

        self.window.close()


class Show_current_transactions:
    

    def __init__(self):

        self.data= [list(transaction.values()) for transaction in Save_transactions_json.load_transaction_data()]
        self.headings = ["Type", "Category", "Description","Amount"]
        self.layout = [
            [sg.Text("Current Transactions")],
            [sg.Table(values=self.data, headings= self.headings,auto_size_columns= True, justification= "Center" , enable_events= True,num_rows= 10, key="-TRANSACTION_LIST-", )],
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
                Report.download_report()

            elif event == "Load Report":
                Report.load_report()

        self.window.close()