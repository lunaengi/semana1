#8. Clasificación de IMC

# Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra
#    "Bajo peso" si es menor a 18.5
#    "Normal" si está entre 18.5 y 24.9
#   "Sobrepeso" si está entre 25 y 29.9
#   "Obesidad" si es mayor o igual a 30

def clasificar_imc():


    peso = float(input("Di su peso en kg: "))
    altura = float(input("Di su altura en mt: "))


    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}")


    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc <= 24.9:
        print("Normal")
    elif 25 <= imc <= 29.9:
        print("Sobrepeso")
    else:
        print("Obesidad")


clasificar_imc()
