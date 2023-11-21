import os
import time
import re
import minijuego_pokemon 
from busqueda_pokemon import buscar_nombre, buscar_id, cargar_datos_pokemon, mostrar_pokemon, guardar_historial
from graficas import cargar_datos_pokemon, graficatipos, graficastats, graficacolores, infostatsid, mostrarestadistica

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

def menu_minijuego():
    while True:
        limpiar_pantalla()
        print("Menú de Minijuegos\n")
        print("1. Adivina el Pokémon")
        print("2. Adivina el Tipo de Color")
        print("3. Frecuencia de Tipos (Solo son los primeros 151 pokemones)")
        print("4. Salir")
        
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            minijuego_pokemon.adivina_el_pokemon()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "2":
            limpiar_pantalla()
            minijuego_pokemon.tipo_color()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "3":
            limpiar_pantalla()
            minijuego_pokemon.frecuencia_tipos()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "4":
            limpiar_pantalla()
            print("\n¡Hasta luego!")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Elige una opción válida del [1-4].")
            time.sleep(2)

def menu_busqueda():
    datos_pokemones = cargar_datos_pokemon()
    while True:
        limpiar_pantalla()
        print("Menú de Búsqueda de Pokémon\n")
        print("1. Buscar por Nombre")
        print("2. Buscar por ID de Pokédex")
        print("3. Salir")
        
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            while True:
                nombre = input("\nIngresa el nombre del Pokémon [A-Z/a-z/-]: ")
                if re.match("^[A-Za-z\s-]*$", nombre):  # Validar que solo contenga letras, espacios y guiones
                    pokemon = buscar_nombre(datos_pokemones, nombre)
                    mostrar_pokemon(pokemon)
                    guardar_historial(pokemon)
                    input("\nPresiona Enter para continuar...")
                    break
                else:
                    print("Nombre no válido. Ingresa solo letras, espacios y guiones.")
                    input("\nPresiona Enter para continuar...")
        elif opcion == "2":
            limpiar_pantalla()
            while True:
                id = input("\nIngresa el ID de Pokédex del Pokémon [1-151]: ")
                if re.match("^[0-9]*$", id):
                    pokemon = buscar_id(datos_pokemones, id)
                    mostrar_pokemon(pokemon)
                    guardar_historial(pokemon)
                    input("\nPresiona Enter para continuar...")
                    break
                else:
                    print("ID no válido. Ingresa solo números.")
                    input("\nPresiona Enter para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            print("¡Hasta luego!")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Elige una opción válida [1-3].")
            time.sleep(2)
        

def menu_graficas():
    datos_pokemones = cargar_datos_pokemon()
    while True:
        limpiar_pantalla()
        print("Menú de Gráficas\n")
        print("1. Gráfico 'tipos de Pokemon' Primera Generacion")
        print("2. Gráfico 'tipos de color' Primera Generacion")
        print("3. Gráfico 'Estadisticas de un Pokemon por ID'")
        print("4. Gráfico 'Estadisticas de un Pokemon por nombre'")
        print("5. Estadisticas promediadas")
        print("6. Salir")

        opcion_graficas = input("\nElige una opción: ")

        if opcion_graficas == "1":
            limpiar_pantalla()
            graficatipos()
            input("\nPresiona Enter para continuar...")
        elif opcion_graficas == "2":
            limpiar_pantalla()
            graficacolores()
            input("\nPresiona Enter para continuar...")
        elif opcion_graficas == "3":
            limpiar_pantalla()
            id = input("\nIngresa el ID de Pokédex del Pokémon [1-151]: ")
            if re.match("^[0-9]*$", id):
                pokemon = buscar_id(datos_pokemones, id)
                infostatsid(pokemon)
                graficastats(pokemon)
                input("\nPresiona Enter para continuar...")
            else:
                print("ID no válido. Ingresa solo números.")
                input("\nPresiona Enter para continuar...")
        elif opcion_graficas == "4":
            limpiar_pantalla()
            nombre = input("\nIngresa el nombre del Pokémon [A-Z/a-z/-]: ")
            if re.match("^[A-Za-z\s-]*$", nombre):  # Validar que solo contenga letras, espacios y guiones
                pokemon = buscar_nombre(datos_pokemones, nombre)
                infostatsid(pokemon)
                graficastats(pokemon)
                input("\nPresiona Enter para continuar...")
            else:
                print("ID no válido. Ingresa solo números.")
                input("\nPresiona Enter para continuar...")
        elif opcion_graficas == "5":
            limpiar_pantalla()
            mostrarestadistica()
            input("\nPresiona Enter para continuar...")
        elif opcion_graficas == "6":
            limpiar_pantalla()
            print("Volviendo al Menú Principal...")
            time.sleep(1)
            break
        else:
            print("Opción no válida. Elige una opción válida [1-5].")
            time.sleep(2)

def menu_principal():
    while True:
        limpiar_pantalla()
        print("Menú Pokemon\n")
        print("1. Búsqueda")
        print("2. Minijuegos")
        print("3. Gráficas")
        print("4. Salir")

        opcion = input("\nIngresa una opción: ")
        if opcion == "1":
            limpiar_pantalla()
            menu_busqueda() # Llama al menú de busqueda
        elif opcion == "2":
            limpiar_pantalla()
            menu_minijuego()  # Llama al menú de minijuegos
        elif opcion == "3":
            limpiar_pantalla()
            menu_graficas() #Llama al menu de graficas
        elif opcion == "4":
            limpiar_pantalla()
            print("¡Gracias por usar la Pokedex!")
            time.sleep(4)
            break
        else: 
            print("\nIngresa una opción correcta [Espere un segundo]")
            time.sleep(2)

if __name__ == "__main__":
    menu_principal()

