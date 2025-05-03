# 9 Año Bisiesto
# Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

try:
    año = int(input("Por favor, ingrese un año: "))


    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es un año bisiesto.")
    else:
        print(f"El año {año} no es un año bisiesto.")

except ValueError:
    print("Error: Debe ingresar un número entero válido para el año.")