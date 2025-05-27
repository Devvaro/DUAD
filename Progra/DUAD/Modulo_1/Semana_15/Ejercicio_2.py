def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort)-1,0,-1):
        if_changes = False
        for index in range(outer_index, 0,-1,):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index - 1]

            print(f'iteration {outer_index},{index}. Current element: {current_element}. Next element: {next_element}')

            if current_element> next_element:
                print('swapping')
                list_to_sort[index]= next_element
                list_to_sort[index - 1] = current_element
                if_changes = True

        if not if_changes:
            break



test_list = [10,7,5,3,2,1]

bubble_sort(test_list)
print(test_list)