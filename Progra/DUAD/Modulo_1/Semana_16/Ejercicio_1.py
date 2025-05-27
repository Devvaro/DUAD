def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        if_changes = False
        for index in range(0, len(list_to_sort)-1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            print(f'iteration {outer_index},{index}. Current element: {current_element}. Next element: {next_element}')

            if current_element> next_element:
                print('swapping')
                list_to_sort[index]= next_element
                list_to_sort[index + 1] = current_element
                if_changes = True

        if not if_changes:
            break



test_list = [3, 4, 8 , 6, 7, 10]
bubble_sort(test_list)

print(test_list)



