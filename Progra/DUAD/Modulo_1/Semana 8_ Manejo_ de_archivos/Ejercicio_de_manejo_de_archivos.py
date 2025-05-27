def lista_de_canciones(file_1, file_2):
    with open(file_1, "r") as file:
        canciones= file.readlines()
        canciones.sort()
    with open(file_2, "w") as file:
        for cancion in canciones:
            file.write(cancion + "\n")
        


file_1= "Canciones.txt"
file_2= "Canciones_ordenadas.txt"


lista_de_canciones(file_1,file_2)