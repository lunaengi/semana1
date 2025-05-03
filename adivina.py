#6. Adivina el Número 8
#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.


def adivina_el_numero():
    secreto = 7
    try:
        intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return
    if intento < secreto:
        print("Tu número es menor que el número secreto.")
    elif intento > secreto:
        print("Tu número es mayor que el número secreto.")
    else:
        print("¡Correcto! Adivinaste el número secreto.")

if __name__ == "__main__":
    adivina_el_numero()