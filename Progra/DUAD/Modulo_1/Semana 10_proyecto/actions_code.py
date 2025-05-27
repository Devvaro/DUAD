students_list=[]

def insert_student_data():
        try:
            full_name=input("Insert student's full name: ")
            class_name= input("Insert class number (ex: 11B): ")
            spanish_grade= int(input("Insert spanish grade: "))
            english_grade= int(input("Insert english grade: "))
            socials_grade= int(input("Insert socials grade: "))
            science_grade= int(input("Insert science grade: "))
            average = (spanish_grade+english_grade+socials_grade+science_grade)/4

            students_dict={
            "full name":full_name,
            "class name":class_name,
            "spanish grade":spanish_grade,
            "english grade":english_grade,
            "socials grade":socials_grade,
            "science grade":science_grade, 
            "average":average
            }
            
        except ValueError:
            print("the value inserted is not between 0 and 100")

        students_list.append(students_dict)

        add_other_user= input("Do you want to add another user? (yes/no): ")
        if add_other_user.lower != "yes":
            print("")


def add_another_user():
    global students_list
    print("This is your current list of students:")
    result = [ {key: value for key, value in student.items() if key != "average"} for student in students_list ]
    print(result)
    



def top_3_average_students():
    global students_list

    if len(students_list) < 3:
        print("Not enough students to display top 3 averages.")
        return

    top_students = sorted(students_list, key=lambda student: student["average"], reverse=True)[:3]

    print("Top 3 students by average grade:")
    for student in top_students:
        print(f"{student['full name']} - Average grade: {student['average']}")



def total_average():
    global students_list

    total = sum(student["average"] for student in students_list)
    average = total / len(students_list)

    print(f"the average of all average in students notes is: {average}")