import random
numero_secreto = random.randint (1,10)



while True:
    numero = int(input("Ingrese un numero del 1 al 10: "))
    if numero == numero_secreto:
        print("Felicidades, adivinaste el numero secreto")
        break
    else:
        print('Incorrecto, intentalo de nuevo')