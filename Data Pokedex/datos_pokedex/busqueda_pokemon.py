import json
from pathlib import Path # --> ayuda a encontrar mejor la ruta en cualquier equipo

def cargar_datos_pokemon():
    consultajson = Path(__file__).parent.parent / 'Consulta de API' / 'pokemones_[13-11_2.14].json'
    with open(consultajson, "r", encoding="utf-8") as archivo_json:
        datos_pokemones = json.load(archivo_json)
    return datos_pokemones

def guardar_historial(pokemon_info): # --> Aqui se genera el txt cuando el usuario ingrese el nombe o id de un pokemon en el menu de busqueda 
    pathtxt = Path(__file__).parent.parent / 'Consulta de API' / 'pokemones_historial.txt' # --> Se guardara en la carpeta de 'Consulta de API'
    with open(pathtxt, "a", encoding='utf-8') as historial:
        if pokemon_info:
            ca = round(pokemon_info['Altura'] * 0.1, 2) # --> hace la conversion de su altura
            cp = round(pokemon_info['Peso'] * 0.1, 2) # --> hace la conversion de su peso
            historial.write(f"Nombre: {pokemon_info['Nombre']}\n")
            historial.write(f"Especie: {pokemon_info['Especie']}\n")
            historial.write(f"Descripción en Español: {pokemon_info['Descripción en Español']}\n")
            historial.write(f"Tipo/s: {', '.join(pokemon_info['Tipo/s'])}\n")
            historial.write(f"Altura: {pokemon_info['Altura']} decímetros, --> {ca} Metros\n")
            historial.write(f"Peso: {pokemon_info['Peso']} hectogramos, --> {cp} Kilogramos\n")
            historial.write(f"Generación: {pokemon_info['Generación']}\n")
            historial.write(f"Hábitat: {pokemon_info['Hábitat']}\n")
            historial.write(f"Tipo de Color: {pokemon_info['Tipo de Color']}\n")
            historial.write(f"Linea Evolutiva: {', '.join(pokemon_info['Linea Evolutiva'])}\n")
            historial.write("Estadísticas:\n")
            historial.write(f"Base Hp: {pokemon_info['Estadísticas']['Base Hp']}, Base Attack: {pokemon_info['Estadísticas']['Base Attack']}, Base Defense: {pokemon_info['Estadísticas']['Base Defense']}\n")  
            historial.write(f"Base Special Attack: {pokemon_info['Estadísticas']['Base Special Attack']}, Base Special Defense: {pokemon_info['Estadísticas']['Base Special Defense']}, Base Speed: {pokemon_info['Estadísticas']['Base Speed']}\n\n")

def buscar_nombre(datos, nombre):
    for pokemon in datos:
        if nombre.lower() == pokemon["Nombre"].lower():
            return pokemon

def buscar_id(datos, id):
    try:
        id = int(id)
        if 1 <= id <= len(datos):
            return datos[id - 1]
    except ValueError:
        return None

def mostrar_pokemon(pokemon):
    if pokemon:
        ca = round(pokemon['Altura'] * 0.1, 2)
        cp = round(pokemon['Peso'] * 0.1, 2)
        print(f"\nNombre: {pokemon['Nombre']}")
        print(f"Tipo/s: {', '.join(pokemon['Tipo/s'])}")
        print(f"Especie: {pokemon['Especie']}")
        print(f"Descripción en Español: {pokemon['Descripción en Español']}")
        print(f"Altura: {pokemon['Altura']} Decimetros", "-->", ca, "Metros")
        print(f"Peso: {pokemon['Peso']} Hectogramos", "-->", cp, "Kilogramos")
        print(f"Generación: {pokemon['Generación']}")
        print(f"Hábitat: {pokemon['Hábitat']}")
        print(f"Tipo de Color: {pokemon['Tipo de Color']}")
        print(f"Linea Evolutiva: {', '.join(pokemon['Linea Evolutiva'])}")
        stats = pokemon["Estadísticas"]
        print("Estadísticas:")
        print(f"Base Hp: {stats['Base Hp']}")
        print(f"Base Attack: {stats['Base Attack']}")
        print(f"Base Defense: {stats['Base Defense']}")
        print(f"Base Special Attack: {stats['Base Special Attack']}")
        print(f"Base Special Defense: {stats['Base Special Defense']}")
        print(f"Base Speed: {stats['Base Speed']}")
    else:
        print("¡No se encontró el Pokémon!")







