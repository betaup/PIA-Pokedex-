import json
import random
import sys
from pathlib import Path

def cargar_datos_pokemon():
    consultajson = Path(__file__).parent.parent / 'Consulta de API' / 'pokemones_[13-11_2.14].json'
    with open(consultajson, "r", encoding="utf-8") as archivo_json:
        datos_pokemones = json.load(archivo_json)
    return datos_pokemones

def mostrar_pokemon(pokemon):
    if pokemon:
        print(f"\nNombre: {pokemon['Nombre']}")
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

if __name__ == "__main__":
    tam = len(sys.argv)
    for argumento in sys.argv:
        if argumento == "-pokemon":
            # Obtenemos los datos de los Pokémon
            datos_pokemones = cargar_datos_pokemon()

            # Generamos un Pokémon aleatorio
            pokemon_aleatorio = random.choice(datos_pokemones)

            # Mostramos el nombre y las estadísticas del Pokémon aleatorio
            print(f"\nNombre: {pokemon_aleatorio['Nombre']}")
            print("Estadísticas:")
            print(f"Base Hp: {pokemon_aleatorio['Estadísticas']['Base Hp']}")
            print(f"Base Attack: {pokemon_aleatorio['Estadísticas']['Base Attack']}")
            print(f"Base Defense: {pokemon_aleatorio['Estadísticas']['Base Defense']}")
            print(f"Base Special Attack: {pokemon_aleatorio['Estadísticas']['Base Special Attack']}")
            print(f"Base Special Defense: {pokemon_aleatorio['Estadísticas']['Base Special Defense']}")
            print(f"Base Speed: {pokemon_aleatorio['Estadísticas']['Base Speed']}")