#7. Mayor de Dos Números
#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

numer1 = int (input("di un numero"))
numer2 = int (input("di otro numero"))

if numer1 > numer2 :
 print ("primer numero es mayor que el segundo")
if numer2 > numer1 :
 print ("segungo numero es mayor que el primer")
else:
 print("son iguales")
