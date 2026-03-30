n = 0
A = []
while True:
    try:
        m = int(input("Ingrese la cantidad de números que va a agregar: "))
        break
    except ValueError:
        print("Valor no valido, digite un número entero.")

while n < m:
    try:
        numero = int(input(f"Ingrese número {n + 1}: "))
        A.append(numero)
        n += 1
    except ValueError:
        print("Valor no valido, digite un número entero.")
        n = 0
        A.clear()

print(f"El mayor es: {max(A)}\nEl menor es: {min(A)}")

#Algoritmo de complejidad O(n) (lineal)
#Recorre la lista una sola vez para encontrar el número mayor y el número menor.