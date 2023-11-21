import json
import random 
import re
from collections import Counter
from pathlib import Path

def cargar_datos_pokemon():
    consultajson = Path(__file__).parent.parent / 'Consulta de API' / 'pokemones_[13-11_2.14].json'
    with open(consultajson, "r", encoding="utf-8") as archivo_json:
        datos_pokemones = json.load(archivo_json)
    return datos_pokemones

def adivina_el_pokemon():
    datos_pokemones = cargar_datos_pokemon()
    pokemon = random.choice(datos_pokemones)
    nombre_pokemon = pokemon["Nombre"]
    tipos_pokemon = ", ".join(pokemon["Tipo/s"])
    especie_pokemon = pokemon["Especie"]
    primeras_letras = nombre_pokemon[:4]
    
    print(f"¡Adivina el Pokémon!\n")
    print(f"Pista 1: Las primeras cuatro letras del nombre del Pokémon son '{primeras_letras}...'")
    print(f"Pista 2: Es un Pokémon de tipo '{tipos_pokemon}'")
    print(f"Pista 3: La especie del Pokémon es '{especie_pokemon}'\n")
    
    intentos = 3
    while intentos > 0:
        respuesta = input("\nIngresa el nombre del Pokémon [A-Z/a-z/-]: ").strip()  # Eliminar espacios extra
        if re.match("^[A-Za-z\s-]*$", respuesta):  # Verificar si la respuesta contiene solo letras y espacios
            if respuesta.lower() == nombre_pokemon.lower():
                print(f"\n¡Correcto! ¡Has adivinado el Pokémon, es '{nombre_pokemon}'!")
                break
            else:
                print(f"\nRespuesta incorrecta. Te quedan {intentos - 1} intento(s).")
                intentos -= 1
        else:
            print("Respuesta no válida. Ingresa solo letras y espacios.")
    
    else:
        print(f"\nSe te acabaron los intentos. El Pokémon era '{nombre_pokemon}'.")

def tipo_color():
    datos_pokemones = cargar_datos_pokemon()
    pokemon = random.choice(datos_pokemones)
    nombre_pokemon = pokemon["Nombre"]
    color_correcto = pokemon["Tipo de Color"]

    print(f"¡Adivina el Tipo de Color del Pokémon '{nombre_pokemon}'!. \nEscribe su tipo de color en idioma 'ingles'")
    
    intentos = 3
    while intentos > 0:
        respuesta = input("\nIngresa el Tipo de Color [A-Z/a-z]: ").strip()  
        if re.match("^[A-Za-z\s]*$", respuesta):  
            if respuesta.lower() == color_correcto.lower():
                print("\n¡Correcto! Su Tipo de Color es", color_correcto)
                break
            else:
                print(f"\nRespuesta incorrecta. Te quedan {intentos - 1} intento(s).")
                intentos -= 1
        else:
            print("Respuesta no válida. Ingresa solo letras y espacios.")
    else:
        print("\nSe te acabaron los intentos, la respuesta correcta es:", color_correcto)

def frecuencia_tipos():
    datos_pokemones = cargar_datos_pokemon()

    tipos = list()
    for pokemon in datos_pokemones:
        tipos.extend(pokemon.get("Tipo/s", []))

    frecuencia_tipos = Counter(tipos)

    print('{0:18}{1:18}'.format("Tipo de Pokémon", "Frecuencia"))
    for tipo, frecuencia in frecuencia_tipos.items():
        print('{0:20}{1:5}'.format(tipo, frecuencia))


















