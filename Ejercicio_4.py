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

B = A.copy()

n = len(A)
for i in range(n):
    mezcla = False
    for j in range(0, n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            mezcla = True
    if not mezcla: break

print(f"Lista origiinal: {B}\nLista ordenada: {A}")

#Algoritmoo de complejidad O(n^2) (cuadrática)
#Recorre la lista n veces para ordenar los números al comparar el número actual con el siguiente, siendo n la longitud de la lista.