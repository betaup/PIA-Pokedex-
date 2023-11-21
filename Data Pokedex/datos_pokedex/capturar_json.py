import requests
import json

# URL base de la API de Pokémon
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
SPECIES_BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"

# Inicializar una lista para almacenar la información de los Pokémon
lista_pokemones = []

# Función para obtener información específica de un Pokémon
def obtener_informacion_pokemon(numero):
    url_pokemon = f"{BASE_URL}{numero}/"
    url_especies = f"{SPECIES_BASE_URL}{numero}/"
    
    response_pokemon = requests.get(url_pokemon)
    response_especies = requests.get(url_especies)

    if response_pokemon.status_code == 200 and response_especies.status_code == 200:
        datos_pokemon = response_pokemon.json()
        datos_especies = response_especies.json()

        # Filtrar y obtener los datos específicos que deseas
        nombre = datos_pokemon['name']
        genero = datos_especies['genera'][5]['genus']
        descripcion_espanol = ""
        for e in datos_especies['flavor_text_entries']:
            if e['language']['name'] == 'es':
                descripcion_espanol = e['flavor_text'].replace("\n", " ")
                break  
        response_evo_chain= requests.get(datos_especies['evolution_chain']['url'])
        if response_evo_chain.status_code == 200: 
            datos_evo_chain = response_evo_chain.json()
            evo_chain = cadena_evol(datos_evo_chain)
        tipos = [tipo['type']['name'] 
                 for tipo in datos_pokemon['types']]
        altura = datos_pokemon['height']
        peso = datos_pokemon['weight']
        generacion = datos_especies['generation']['name']
        habitat = datos_especies['habitat']['name']
        colores = datos_especies['color']['name']
        stats = [sts['base_stat']
                 for sts in datos_pokemon['stats']]
        
         # Crear un diccionario con la información del Pokémon
        pokemon_info = {
            "Nombre": nombre,
            "Especie": genero,
            "Descripción en Español": descripcion_espanol,
            "Tipo/s": tipos,
            "Altura": altura,
            "Peso": peso,
            "Generación": generacion,
            "Hábitat": habitat,
            "Tipo de Color": colores,
            "Linea Evolutiva": evo_chain,
            "Estadísticas": {
                "Base Hp": stats[0],
                "Base Attack": stats[1],
                "Base Defense": stats[2],
                "Base Special Attack": stats[3],
                "Base Special Defense": stats[4],
                "Base Speed": stats[5]
            }
        }

        # Agregar la información del Pokémon a una lista
        lista_pokemones.append(pokemon_info)

def cadena_evol (datos):
    cad = list()
    evo_chain = datos['chain']['species']['name']
    cad.append(evo_chain)
    if datos['chain']['evolves_to'] != []:
        for e in range(len(datos['chain']['evolves_to'])):
            evo_chain =  datos['chain']['evolves_to'][e]['species']['name']
            cad.append(evo_chain)
            if datos['chain']['evolves_to'][e]['evolves_to'] != []:
                for d in range(len(datos['chain']['evolves_to'][e]['evolves_to'])):
                    evo_chain=  datos['chain']['evolves_to'][e]['evolves_to'][d]['species']['name']
                    cad.append(evo_chain)
    return cad


if __name__ == "__main__":
    for numero in range(1, 152):  # Obtener datos de los primeros 150 Pokémon
        obtener_informacion_pokemon(numero)

    # Guardar la información de los Pokémon en un archivo JSON
    with open("pokemones.json", "w", encoding="utf-8") as archivo_json:
        json.dump(lista_pokemones, archivo_json, ensure_ascii=False, indent=4)

    print("La información de los Pokémon se ha guardado en 'pokemones.json'.")
