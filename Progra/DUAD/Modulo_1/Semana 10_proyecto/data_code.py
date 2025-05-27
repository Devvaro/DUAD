import csv
from actions_code import students_list


def export_to_csv(files='students.csv', data=None, headers=None):

    if data is None:
        data= students_list
    if headers is None:
        headers= students_list[0].keys()
    
    with open(files, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)



def import_csv(files):
    with open(files, mode='r', encoding='utf-8') as file:
        reader= csv.DictReader(file)
        students=list(reader)
        for row in reader:
            print(row)
        print(students)

