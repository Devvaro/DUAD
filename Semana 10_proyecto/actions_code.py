def insert_student_data():

    student_data= []
    
    Students={
        "full name":input("Insert student's full name: "),
        "class name":input("Insert class number (ex: 11B): "),
        "spanish grade":int(input("Insert spanish grade: ")),
        "english grade":int(input("Insert english grade: ")),
        "socials grade":int(input("Insert socials grade: ")),
        "science grade":int(input("Insert science grade: ")),
        "add another user": input("Do you want to add another user?: ")
    }
    student_data.append(Students)


    for average in Students:
        sum(Students["english grade","spanish grade","socials grade","science grade"]) /4
        

    while Students["add another user"]== "yes":
        insert_student_data()
    else:
        from menu_code import menu


insert_student_data()



