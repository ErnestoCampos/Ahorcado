# Juego del Ahorcado
print("============================================")
print("=== Bienvenido a el juego del ahoracado! ===")
print("============================================")

palabra = str(input("Ingresa la palabra a adivinar: "))
lista_de_acertados = []


def Ahorcado():
    pv = 6
    while True:
        letra = input("ingrese una letra: ")
        if letra in palabra:
            lista_de_acertados.append(letra)
            palabras = [letra if letra in lista_de_acertados else '-' for letra in palabra]
            print(palabras)
            if palabras == list(palabra):
                print(f"Adivinaste la palabra {palabra}!, ganaste el juego!") 
                return
        elif pv == 0: 
            print(f"Perdiste el juego, te quedaste sin vidas :(")
            return
        else:
            pv -= 1
            print(f"Incorrecto, vidas restantes: {pv}") 

Ahorcado()

