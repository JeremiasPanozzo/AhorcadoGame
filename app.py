import juego
import os
import platform

#limpia la consola
def limpiar_consola():
    sistema = platform.system()  # Obtiene el nombre del sistema operativo
    
    if sistema == "Windows":
        os.system("cls")  # Comando para limpiar la consola en Windows
    else:
        os.system("clear") 


# Función para mostrar el menú principal
def menu():
    
    print("!Bienvenido al juego del ahorcado!\n")
    print("Seleccione una opción:\n")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    
    
#juego del ahorcado
def juego_ahorcado():

    lista_palabras = ['manzana', 'ventana', 'sol', 'luna', 'arbol', 'nube', 'cielo', 'mar',
    'río', 'montaña', 'ciudad', 'amor', 'fuego', 'agua', 'puerta', 'espejo',
    'estrella', 'silla', 'libro', 'coche', 'música', 'café', 'fruta', 'lago',
    'camisa', 'ratón', 'escritorio', 'flor', 'risa', 'piedra', 'tren', 'nieve',
    'avión', 'barco', 'pelota', 'plato', 'dibujo', 'solución', 'mesa', 'puente'
    ]

    palabra = juego.generar_palabra(lista_palabras)
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

if __name__ == "__main__":
    
    limpiar_consola()
    
    menu()

    opcion = int(input("\nOpcion: "))

    if opcion == 1:
        limpiar_consola()
        juego_ahorcado()
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    else:
        print("Opcion invalida")
    
