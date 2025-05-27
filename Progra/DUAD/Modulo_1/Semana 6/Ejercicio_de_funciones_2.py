variable_outside_function_scope = 7

def print_variable():
  print(f'Inside function: {variable_outside_function_scope}')


print_variable()


def print_change_variable():
    variable_outside_function_scope= 8
    print(f'Outside function: {variable_outside_function_scope}')


print_change_variable()