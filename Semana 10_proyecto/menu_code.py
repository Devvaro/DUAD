def menu():
    while True:
        try:
            x=int(input("insert a number from 1 to 6: "))
            break
        except ValueError:
            print("the number inserted is not a number")
    if x>6:
        try:
            x=int(input("insert a number from 1 to 6: "))

        except ValueError:
            print("the number inserted is not a value from 1 to 6")

    if x==1:
        from actions_code import insert_student_data
    elif x==2:
        student_database()
    elif x==3:
        top_3_students()
    elif x==4:
        students_notes_average()
    elif x==5:
        export_data_to_csv()
    elif x==6:
        import_data_from_csv()

menu()