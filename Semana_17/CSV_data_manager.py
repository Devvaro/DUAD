import FreeSimpleGUI as sg
import csv

def download_report():
    from Visual_windows import Transaction_manager
    transaction=Transaction_manager.load_transaction_data()

    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction tracker"])
        writer.writerow(["Type", "Category", "Description", "Amount"])
        for item in transaction:
            writer.writerow([item["type"], item["category"], item["description"], item["amount"]])
        
    sg.popup("Report downloaded successfully")


def load_report():
    with open("report.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)