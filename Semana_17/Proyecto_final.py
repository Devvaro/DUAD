import FreeSimpleGUI as sg
import json
import csv

def save_categories(categories):
    with open("categories.json", "w") as file:
        json.dump(categories, file)


def load_categories():
    try:
        with open("categories.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def category_window():
    categories = load_categories()

    layout = [
        [sg.Text("Category Manager")],
        [sg.Listbox(categories, size=(30, 5), key="-CATEGORY_LIST-")],
        [sg.Input(key="-NEW_CATEGORY-"), sg.Button("Add Category")],
        [sg.Button("Save & Exit")]
    ]

    window = sg.Window("Categories", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Save & Exit"):
            save_categories(categories)  
            break

        elif event == "Add Category":
            new_category = values["-NEW_CATEGORY-"].strip()

            if new_category and new_category not in categories:
                categories.append(new_category)
                window["-CATEGORY_LIST-"].update(categories)  

    window.close()


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def transaction_window(transaction_type):
    transaction_type = ["Expense", "Income"]
    categories = load_categories()
    layout = [
        [sg.Text("transaction Tracker")],
        [sg.Text("Type of Transaction"), sg.Combo(transaction_type, key="-TRANSACTION_TYPE-", size=(20, 3))],
        [sg.Text("Description"), sg.Input(key="-DESCRIPTION-")],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY-", size=(20, 3))],
        [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window = sg.Window("Transaction", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        elif event == "Save":
            transaction_type = values["-TRANSACTION_TYPE-"]
            category = values["-CATEGORY-"]
            description = values["-DESCRIPTION-"]
            amount = values["-AMOUNT-"]

            if transaction_type and category and description and amount:
                data = load_data()
                data.append({"type": transaction_type, "category": category, "description": description, "amount": amount})
                save_data(data)
                sg.popup(f"{transaction_type} saved successfully")
                break
            else:
                sg.popup("Please fill in all fields")

        elif amount.isnumeric():
            try:
                amount = float(amount)
                return True
            except ValueError:
                sg.popup("Please enter a valid number")
                continue

    window.close()


def show_current_transactions():
    data = load_data()
    layout = [
        [sg.Text("Current Transactions")],
        [sg.Listbox(data, size=(100, 10), key="-TRANSACTION_LIST-")],
        [sg.Button("Back")]
    ]

    window = sg.Window("Transactions", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Back"):
            break

    window.close()

def download_report():
    transaction=load_data()

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

def show_report():

    layout = [
        [sg.Text("Report")],
        [sg.Button("Download Report"), sg.Button("Load Report")],
        [sg.Button("Back")]
    ]

    window = sg.Window("Report", layout)

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Back"):
            break

        elif event == "Download Report":
            download_report()

        elif event == "Load Report":
            load_report()

    window.close()


def main_menu():
    layout = [
        [sg.Text("Main Menu")],
        [sg.Button("Manage Categories"), sg.Button("Add transaction")],
        [sg.Button("Show transactions tracker"), sg.Button("Show Report")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Expense Tracker", layout)

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        elif event == "Manage Categories":
            category_window() 

        elif event == "Add transaction":
            transaction_window("Expense")

        elif event == "Show transactions tracker":
            show_current_transactions()

        elif event == "Show Report":
            show_report()


    window.close()


main_menu()