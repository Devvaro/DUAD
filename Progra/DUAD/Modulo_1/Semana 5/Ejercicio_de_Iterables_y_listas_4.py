def odd_number(list):
    New_list=[]
    for element in list:
        if element % 2 == 0:
            New_list.append(element)
    return New_list


List=[1,2,3,4,5,6,7,8,9,42,72,91,102,204,372,1001]

without_odd_numbers= odd_number(List)

print("List:", List)
print("Without Odd Numbers:",without_odd_numbers)