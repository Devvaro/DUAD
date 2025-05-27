def print_first_arg(func):
    def wrapper(*args):
        print(f'funcion con argumentos:{args} ')
        result= func(*args)
        print(f'resultado de la funcion: {result}')
        return result
    return wrapper

@print_first_arg
def sum_values(a,b):
    return a + b


sum_values(10,20)