import juego
import os
import platform

def limpiar_consola():
    sistema = platform.system()  # Obtiene el nombre del sistema operativo
    
    if sistema == "Windows":
        os.system("cls")  # Comando para limpiar la consola en Windows
    else:
        os.system("clear") 

def juego_ahorcado():

    limpiar_consola()

    lista_palabras = ['manzana', 'ventana', 'sol', 'luna', 'arbol', 'nube', 'cielo', 'mar',
    'río', 'montaña', 'ciudad', 'amor', 'fuego', 'agua', 'puerta', 'espejo',
    'estrella', 'silla', 'libro', 'coche', 'música', 'café', 'fruta', 'lago',
    'camisa', 'ratón', 'escritorio', 'flor', 'risa', 'piedra', 'tren', 'nieve',
    'avión', 'barco', 'pelota', 'plato', 'dibujo', 'solución', 'mesa', 'puente'
    ]

    palabra = juego.generar_palabra(lista_palabras)
    letras_adivinadas = set()
    intentos = 7

    print("¡Bienvenido al juego del ahorcado!",f"\nTienes {intentos} intentos para adivinar la palabra")
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
        print(f"Palabra de {len(palabra)} letra")
        if set(palabra) <= letras_adivinadas:
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break
    else:
        print("\nHas perdido. La palabra era:", palabra)

if __name__ == "__main__":
    juego_ahorcado()
