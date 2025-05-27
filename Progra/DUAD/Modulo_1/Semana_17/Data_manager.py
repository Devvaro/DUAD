import FreeSimpleGUI as sg
import csv
import json
from Logic import Logic_report

class Save_categories_json:
    FILE_NAME = "categories.json"

    @staticmethod
    def save(categories):
        with open(Save_categories_json.FILE_NAME, "w") as file:
            json.dump(categories, file)

    @staticmethod
    def load():
        try:
            with open(Save_categories_json.FILE_NAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


class Save_transactions_json:
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



class Report:
    FILE_NAME = "report.csv"

    @staticmethod
    def download_report():
        if Logic_report.not_transactions():
            return
        
        transaction = Save_transactions_json.load_transaction_data()

        with open("report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Transaction tracker"])
            writer.writerow(["Type", "Category", "Description", "Amount"])
            for item in transaction:
                writer.writerow([item["type"], item["category"], item["description"], item["amount"]])

        sg.popup("Report downloaded successfully")


    @staticmethod
    def load_report():
        with open("report.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)