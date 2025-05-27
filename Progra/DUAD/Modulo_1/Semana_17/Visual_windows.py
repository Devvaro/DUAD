import FreeSimpleGUI as sg
from Logic import Transaction, Category
from Data_manager import Save_categories_json, Save_transactions_json, Report
class Categories_window:

    def __init__(self):

        self.categories = Save_categories_json.load()
        self.layout = [
            [sg.Text("Category Manager")],
            [sg.Listbox(self.categories, size=(30, 5), key="-CATEGORY-", enable_events=True)],
            [sg.Input(key= "-NEW_CATEGORY-"), sg.Button("Add Category")],
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
                new_category = values["-NEW_CATEGORY-"].strip()
                category_instance = Category(new_category)

                if category_instance.is_valid(self.categories):
                    self.categories.append(new_category)
                    self.window["-CATEGORY-"].update(self.categories)
                    
                else:
                    sg.popup_error("Invalid category name or already exists")


        self.window.close()


class Transaction_manager_window:

    def __init__(self):
        self.categories = Save_categories_json.load()
        self.transaction_type= ["Income", "Expense"]
        self.layout = [
            [sg.Text("transaction Tracker")],
            [sg.Text("Type of Transaction"), sg.Combo(self.transaction_type, key= "-TRANSACTION_TYPE-", size=(20, 3))],
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
                transaction= Transaction(
                    values["-TRANSACTION_TYPE-"],
                    values["-CATEGORY-"],
                    values["-DESCRIPTION-"],
                    values["-AMOUNT-"]
                )

                if transaction.is_valid():
                    data= Save_transactions_json.load_transaction_data()
                    data.append(transaction.to_dict())
                    Save_transactions_json.save_transaction_data(data)
                    sg.popup(f"{transaction.transaction_type} saved successfully")
                    break
                else:
                    sg.popup_error("Please fill in all fields correctly (Amount must be a positive number)")

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