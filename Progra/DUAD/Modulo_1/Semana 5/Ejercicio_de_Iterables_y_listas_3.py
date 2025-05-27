new_list=[1,2,3,4,5,6,7,8,9]

def switch_order(list):
    if len(list) > 1:
        list[0],list[-1]=list[-1],list[0]
    return list

print("List:",new_list)

Change_list = switch_order(new_list)

print("changed list:",Change_list)