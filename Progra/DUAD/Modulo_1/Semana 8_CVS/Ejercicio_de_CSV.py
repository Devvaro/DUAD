import csv

games_list= [
    {
        'nombre':input("Ingrese el nombre del Videojuego: "),
        'genero':input("Ingrese el genero del Videojuego: "),
        'desarrollador':input("Ingrese el desarrollador del Videojuego: "),
        'clasificacion ESRB':input("Ingrese la clasificacion ESRB del Videojuego: "),
    }
]

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file('games.csv', games_list,games_list[0].keys())

