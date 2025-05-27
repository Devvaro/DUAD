from actions_code import students_list

def menu():
    while True:
        try:
            x=int(input("insert a number from 1 to 7: "))
            break
        except ValueError:
            print("the value inserted by user is not a number")
    if x>7:
        try:
            x=int(input("insert a number from 1 to 7: "))
        except ValueError:
            print("the value inserted by user is not part of the menu")

    if x==1:
        from actions_code import insert_student_data
        insert_student_data()
        menu()
    elif x==2:
        from actions_code import add_another_user
        add_another_user()
        menu()
    elif x==3:
        from actions_code import top_3_average_students
        top_3_average_students()
        menu()
    elif x==4:  
        from actions_code import total_average
        total_average()
        menu()
    elif x==5:
        from data_code import export_to_csv
        export_to_csv()
        menu()
    elif x==6:
        from data_code import import_csv
        import_csv('students.csv')
        menu()
    elif x==7:
        print("thank you for using this program")
        exit()


menu()

