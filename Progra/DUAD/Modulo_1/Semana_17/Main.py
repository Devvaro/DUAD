import FreeSimpleGUI as sg
from Visual_windows import Categories_window, Transaction_manager_window, Show_current_transactions, Show_report

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
            category_manager = Categories_window()
            category_manager.run()

        elif event == "Add transaction":
            transaction_manager= Transaction_manager_window()
            transaction_manager.run()

        elif event == "Show transactions tracker":
            transaction_tracker= Show_current_transactions()
            transaction_tracker.run()

        elif event == "Show Report":
            report_tracker= Show_report()
            report_tracker.run()


    window.close()


main_menu()