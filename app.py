import juego
import os
import platform

#listado de palabras
lista_palabras = ['manzana', 'ventana', 'sol', 'luna', 'arbol', 'nube', 'cielo', 'mar',
    'río', 'montaña', 'ciudad', 'amor', 'fuego', 'agua', 'puerta', 'espejo',
    'estrella', 'silla', 'libro', 'coche', 'música', 'café', 'fruta', 'lago',
    'camisa', 'ratón', 'escritorio', 'flor', 'risa', 'piedra', 'tren', 'nieve',
    'avión', 'barco', 'pelota', 'plato', 'dibujo', 'solución', 'mesa', 'puente'
]

#limpia la consola
def limpiar_consola():
    
    """Limpia la consola dependiendo del sistema operativo."""
    comando = "cls" if platform.system() == "Windows" else "clear"
    os.system(comando)

# Función para mostrar el menú principal
def menu():
    """Muestra el menú principal del juego."""
    print("!Bienvenido al juego del ahorcado!\n")
    print("Seleccione una opción:\n")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    
    
#juego del ahorcado
def juego_ahorcado(palabras):

    palabra = juego.generar_palabra(palabras)
    letras_adivinadas = set()
    intentos = 7

    print("¡Bienvenido al juego del ahorcado!\n",f"\nTienes {intentos} intentos para adivinar la palabra")
    print(f"Palabra de {len(palabra)} letra")

    while intentos > 0:
        print("\n" + juego.mostrar_palabra(palabra, letras_adivinadas))
        juego.imprimir_monigote(intentos)

        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos -= 1
            
        limpiar_consola()
        
        if set(palabra) <= letras_adivinadas:
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break
    else:
        print("\nHas perdido. La palabra era:", palabra)

def ejecutar_menu():
    """Ejecuta el menú de selección y las acciones correspondientes."""
    limpiar_consola()

    while True:
        menu()
        
        try:
            opcion = int(input("\nOpción: "))
            if opcion == 1:
                limpiar_consola()
                juego_ahorcado(lista_palabras)
            elif opcion == 2:
                print("\nInstrucciones del juego:")
                print("Debes adivinar la palabra oculta letra por letra.")
                print("Tienes 7 intentos para adivinar la palabra correctamente.")
            elif opcion == 3:
                print("Gracias por jugar. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")
        except ValueError:
            print("Por favor, selecciona una opción válida.")
        
if __name__ == "__main__":
    
    ejecutar_menu()