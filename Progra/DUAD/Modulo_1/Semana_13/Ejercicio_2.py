def check_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg,int):
                raise ValueError(f"El argumento '{arg}' no es un número.")
        return func(*args)
    return wrapper

@check_numbers
def number(a,b):
    return a, b


print(number(20,30))
str(print(number(10,"tres")))