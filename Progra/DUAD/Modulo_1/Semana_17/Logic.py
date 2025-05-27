import FreeSimpleGUI as sg

class Category:
    def __init__(self,name):
        self.name = name

    def is_valid(self, existing_categories):
        return self.name and self.name not in existing_categories
    
    def to_dict(self):
        return {"category": self.name}



class Transaction:

    def __init__(self, transaction_type, description, category, amount):
        self.transaction_type = transaction_type
        self.description = description.strip()
        self.category = category
        self.amount = amount

    def is_valid(self):
        return (
            self.transaction_type 
            and self.description != ""
            and self.category 
            and self.positive_number(self.amount)
        )

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "description": self.description,
            "category": self.category,
            "amount": float(self.amount),
        }

    @staticmethod
    def positive_number(amount):
        try:
            amount= float(amount)
            return amount >=0
        except ValueError:
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
