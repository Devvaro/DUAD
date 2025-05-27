def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1): #0(n)
        if_changes = False #0(1)
        for index in range(0, len(list_to_sort)-1 - outer_index): #0(n)
            current_element = list_to_sort[index] #0(1)
            next_element = list_to_sort[index + 1] #0(1)

            print(f'iteration {outer_index},{index}. Current element: {current_element}. Next element: {next_element}') #0(1)

            if current_element> next_element:  #0(1)
                print('swapping') #0(1)
                list_to_sort[index]= next_element #0(1)
                list_to_sort[index + 1] = current_element #0(1)
                if_changes = True #0(1)

        if not if_changes: #0(1)
            break #0(1)



test_list = [3, 4, 8 , 6, 7, 10] #0(1)
bubble_sort(test_list) #O(2^n)

print(test_list) #0(1)