#5. Calculadora de Propinas 
#pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina. # type: ignore

def calcular_propina():
    try:
        total = float(input("Ingrese el total de la cuenta: €"))
        if total < 0:
            print("El total no puede ser negativo.")
            return
    except ValueError:
        print("Por favor, ingrese un número válido para el total.")
        return

    print("Qué porcentaje de propina quiere dejar?")
    print("Opciones: 10, 15, 20")
    try:
        porcentaje = int(input("Ingrese el porcentaje de propina: "))
        if porcentaje not in [10, 15, 20]:
            print("seleccione un porcentaje válido (10, 15 o 20).")
            return
    except ValueError:
        print("ingrese un número válido para el porcentaje.")
        return

    propina = total * porcentaje / 100
    print(f"El valor de la propina es: €{propina:.2f}")

if __name__ == "__main__":
    calcular_propina()