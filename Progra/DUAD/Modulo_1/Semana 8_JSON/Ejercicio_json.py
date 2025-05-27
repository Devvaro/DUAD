import json


def new_item():
    new_pokemon= [
        {
        "name": input("Ingrese el nombre del pokemon: "), 
        "type": input("Ingrese el tipo de pokemon: "),
        "HP": int(input("Ingrese el HP del pokemon: ")),
        "Attack": int(input("Ingrese el attack del pokemon: ")),
        "Defense": int(input("Ingrese el defense del pokemon: ")),
        "Sp. Attack": int(input("Ingrese sp.attack del pokemon: ")),
        "Sp. Defense": int(input("Ingrese sp.defense del pokemon: ")),
        "Speed": int(input("Ingrese el speed del pokemon: "))
        }
    ]
    return new_pokemon


def json_read_write (file_1,file_2):
    data_to_add = new_item()
    
    with open (file_1, "r" ) as file_to_read:
        convert_to_json= json.load (file_to_read)
    
    convert_to_json.append(data_to_add)

    with open(file_2, "w") as file_to_write:
        json.dump(convert_to_json, file_to_write, indent =1 ) 


file_1= "archivo.json"
file_2= "nuevo_pokemon.json"

json_read_write(file_1,file_2)


