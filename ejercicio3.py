nums = []
n = int(input("Cuantos números vas a ingresar?: "))
for i in range(n):
    num = int(input(f"Ingresar el número {i+1}: "))
    nums.append(num)

buscar = int(input("Ingresar el valor que desea buscar: "))
posicion = -1

for i in range(n): 
    if nums[i] == buscar: 
        posicion = i
        break

if posicion != -1: 
    print(f"El numero {buscar} fue encontrado en la posicion {posicion}")
else: 
    print(f"El numero {buscar} no fue encontrado en el conjunto")

#Complejidad Big O: O(n)
#Justificacion: Es complejidad lineal porque se esta recorriendo la lista un elemento a la vez hasta encontrar una coincidenica o hasta terminar la lista. En el peor caso se revisan n elementos de la lista, por lo que el tiempo de ejecución crece directamente en función de n. 