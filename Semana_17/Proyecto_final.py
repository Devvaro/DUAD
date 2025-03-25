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


def save_expense(expense):
    with open("expense.json", "w") as file:
        json.dump(expense, file)


def load_expense():
    try:
        with open("expense.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def expense_window():
    expense=load_expense()
    categories=load_categories()
    
    layout = [
        [sg.Text("Expense Tracker")],
        [sg.Text("Amount"), sg.Input(key="-EXPENSE-", size=(10, 1))],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY_DROPDOWN-", size=(20, 5))],
        [sg.Button("Add Expense"), sg.Button("Back")],
    ]

    window = sg.Window("Expense Tracker", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Back"):
            save_expense(expense)
            break
            

        elif event == "Add Expense":
            selected_category = values["-CATEGORY_DROPDOWN-"]
            expense_amount = values["-EXPENSE-"]

            if selected_category not in categories:
                sg.popup_error("Category not found, please add it first") 
                break

            if selected_category and expense_amount:
                sg.popup(f"Expense Added: ${expense_amount} to {selected_category}")

            if expense_amount not in expense:
                expense.append(expense_amount)
                window["-EXPENSE-"].update(expense)

            

    window.close()


def save_income(income):
    with open("income.json", "w") as file:
        json.dump(income, file)


def load_income():
    try:
        with open("income.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def income_window():
    income=load_income()
    categories=load_categories()
    

    layout = [
        [sg.Text("Income Tracker")],
        [sg.Text("Amount"), sg.Input(key="-INCOME-", size=(10, 1))],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY_DROPDOWN-", size=(20, 5))],
        [sg.Button("Add Income"), sg.Button("Back")],
    ]

    window = sg.Window("Income Tracker", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Back"):
            save_income(income)
            break
            

        elif event == "Add Income":
            selected_category = values["-CATEGORY_DROPDOWN-"]
            income_amount = values["-INCOME-"]

            if selected_category not in categories:
                sg.popup_error("Category not found, please add it first") 
                break

            if selected_category and income_amount:
                sg.popup(f"Income Added: ${income_amount} to {selected_category}")

            if income_amount not in income:
                income.append(income_amount)
                window["-INCOME-"].update(income)


    window.close()


def download_report():
    categories = load_categories()
    expenses = load_expense()
    income = load_income()

    with open("report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Expenses", "Income"])
        writer.writerows(zip(categories, expenses, income)) 
        
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
        [sg.Button("Manage Categories")],
        [sg.Button("Add expense"), sg.Button("Add Income")],
        [sg.Button("Show Report")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Expense Tracker", layout)

    while True:
        event, _ = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        elif event == "Manage Categories":
            category_window() 

        elif event == "Add expense":
            expense_window()
        
        elif event == "Add Income":
            income_window()

        elif event == "Show Report":
            show_report()


    window.close()


main_menu()