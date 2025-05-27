print("Esta es la calculadora de Python ingrese 1 para Sumar, 2 para Restar, 3 para multiplicar, 4 para dividir, 5 para Borrar resultado")
print("")

def menu():
    while True:
        try:
            x=int(input("Ingrese un numero del 1 al 6: "))
            break
        except ValueError:
            print("El valor digitado no es un numero")
    if x>6:
        try:
            x=int(input("Ingrese un numero del 1 al 6: "))

        except IndexError:
            print("el numero indicado no es un valor del 1 al 6")

    if x==1:
        suma()
    elif x==2:
        resta()
    elif x==3:
        multiplicacion()
    elif x==4:
        division()
    elif x==5:
        borrar_resultado()
    elif x==6:
        salir()


resultado=0

def suma():
    global resultado
    s=int(input("ingrese el valor que quiere sumar: "))
    resultado+= s
    print(f'el resultado de la suma es {resultado}')
    opciones()  


def resta():
    global resultado
    r=int(input("ingrese el valor que quiere restar: "))
    resultado-=r
    print(f'el resultado de la resta es {resultado}')
    opciones()


def multiplicacion():
    global resultado
    m=int(input("ingrese el valor que quiere multiplicar: "))
    resultado*=m
    print(f'el resultado de la multiplicacion es {resultado}')
    opciones()  


def division():
    global resultado
    d=int(input("ingrese el valor que quiere dividir: "))
    resultado/=d
    print(f'el resultado de la division es {resultado}')
    opciones()  


def borrar_resultado():
    global resultado
    borrar_resultado=0
    resultado=borrar_resultado
    print(f'borrando resultado...')
    print(resultado)
    opciones()

def salir():
    while salir:
        print("Gracias por usar la calculadora... Cerrando.")
        break


def opciones():
    menu()


opciones()

