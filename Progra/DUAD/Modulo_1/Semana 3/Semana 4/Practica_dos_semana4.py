nombre=input("Ingrese su Nombre: ")
apellido=input("Ingrese su Apellido: ")
edad=int(input("Ingrese su Edad: "))

if (edad <= 1):
    print (f'Hola {nombre} su categoria es: Bebe')
elif (edad <= 12):
    print (f'Hola {nombre} su categoria es de: Niño')
elif (edad <= 15):
    print (f'Hola {nombre} su categoria es de: Preadolescente')
elif (edad <= 19):
    print (f'Hola {nombre} su categoria es de: Adolescente')
elif (edad <= 30):
    print (f'Hola {nombre} su categoria es de: Adulto joven')
elif (edad <= 60):
    print (f'Hola {nombre} su categoria es de: Adulto')
else:
    print(f'Hola {nombre} su categoria es de: Adulto Mayor')




