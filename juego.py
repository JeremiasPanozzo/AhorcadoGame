import random

# Imprime un monigote según el número de intentos restantes
def imprimir_monigote(intentos_restantes):
    estados = [
        """-------
|      
|     
|      
|      
|     
|_____
""",
        """-------
|      |
|     
|      
|      
|     
|_____
""",
        """-------
|      |
|      O
|      
|      
|     
|_____
""",
        """-------
|      |
|      O
|      |
|      
|     
|_____
""",
        """-------
|      |
|      O
|     /|
|      
|     
|_____
""",
        """-------
|      |
|      O
|     /|\\
|      
|     
|_____
""",
        """-------
|      |
|      O
|     /|\\
|     / 
|     
|_____
""",
        """-------
|      |
|      O
|     /|\\
|     / \\
|     
|_____
"""
    ]
    print(estados[8 - intentos_restantes])

# Genera una palabra aleatoria de una lista
def generar_palabra(lista):
    return lista[random.randint(0, len(lista) - 1)]

# Muestra la palabra con las letras adivinadas y los guiones bajos
def mostrar_palabra(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
