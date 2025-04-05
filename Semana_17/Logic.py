import FreeSimpleGUI as sg

class Logic_transaction_manager:
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


class Logic_report:
    @staticmethod
    def not_transactions():
        from Data_manager import Save_transactions_json
        transaction = Save_transactions_json.load_transaction_data()

        if not transaction:
            sg.popup("No transactions found")
            return True
        
        return False
