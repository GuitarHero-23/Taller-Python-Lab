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

q = len(A)

for i in range(q):
    for j in range(q):
        if i != j:
            print(f"({A[i]}, {A[j]})")

#Algoritmo de complejidad O(n^2) (cuadrática)
#Recorre la lista q^2 veces para imprimir todas las combinaciones posibles de números, siendo q la longitud de la lista.