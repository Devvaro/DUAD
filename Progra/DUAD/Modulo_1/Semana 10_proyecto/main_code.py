def main_menu():
    print("Welcome to the Student Control System")
    print("")
    
    try:
        main=input('type "start" to get to the menu: ')
        if main== "start":
            from menu_code import menu
        menu()
    except UnboundLocalError:
        print("that's not the way to get to the menu ")
        print('')
        main_menu()


main_menu()