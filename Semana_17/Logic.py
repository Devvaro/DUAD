import FreeSimpleGUI as sg
class Transaction:

    def __init__(self):
        self.type = "-TRANSACTION_TYPE-"
        self.description = "-DESCRIPTION-"
        self.amount = "-AMOUNT-"
        self.transaction_type= ["Expense", "Income"]


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
        
    @staticmethod
    def update_transaction(transaction_type, category, description, amount):
        from Data_manager import Save_transactions_json
        data = Save_transactions_json.load_transaction_data()
        data.append({"type": transaction_type, "category": category, "description": description, "amount": float(amount)})
        Save_transactions_json.save_transaction_data(data)



class Category:
    def __init__(self):
        self.category = "-CATEGORY-"
        self.new_category= "-NEW_CATEGORY-"
        

    def add_new_category(self, values, categories, window):
        new_category = values[self.new_category].strip()
        if new_category and new_category not in categories:
            categories.append(new_category)
            window[self.category].update(categories)
        else:
            sg.popup("Category is empty or already exists.")


class Logic_report:
    @staticmethod
    def not_transactions():
        from Data_manager import Save_transactions_json
        transaction = Save_transactions_json.load_transaction_data()

        if not transaction:
            sg.popup("No transactions found")
            return True
        
        return False
