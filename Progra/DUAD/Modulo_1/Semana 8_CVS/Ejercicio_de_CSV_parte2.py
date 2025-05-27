import csv

games_list= [
    {
        'nombre':input("Ingrese el nombre del Videojuego: "),
        'genero':input("Ingrese el genero del Videojuego: "),
        'desarrollador':input("Ingrese el desarrollador del Videojuego: "),
        'clasificacion ESRB':input("Ingrese la clasificacion ESRB del Videojuego: "),
    }
]

def write_csv_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer =csv.writer(file,dialect=csv.excel_tab)
        writer.writerow(games_list[0].items())


write_csv_file('games.csv')

