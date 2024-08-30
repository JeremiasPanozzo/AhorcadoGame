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

def pausar():
    """Función para pausar la ejecución hasta que el usuario presione Enter."""
    input("\nPresiona Enter para continuar...")
    
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
    
    """Ejecuta la lógica principal del juego del ahorcado."""

    palabra = juego.generar_palabra(palabras)
    letras_adivinadas = set()
    letras_incorrectas = set()
    intentos = 7

    print(f"¡Bienvenido al juego del ahorcado!\nTienes {intentos} intentos para adivinar la palabra de {len(palabra)} letras.")

    while intentos > 0:
        
        print("\n" + juego.mostrar_palabra(palabra, letras_adivinadas))
        juego.imprimir_monigote(intentos)
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")

        letra = input("Adivina una letra: ").lower()

        # Validar que sea una letra única
        if len(letra) != 1 or not letra.isalpha():
            print("Entrada no válida. Por favor ingresa una sola letra.")
            pausar()
            limpiar_consola()
            continue
            
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos -= 1
            letras_incorrectas.add(letra)
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
            pausar()
        
        if set(palabra).issubset(letras_adivinadas):
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
            break

        limpiar_consola()
    else:
        print(f"\nHas perdido. La palabra era: {palabra}")

    pausar()

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