nums = []
for i in range(3): 
    num = int(input(f"Ingrese el número {i+1}: ")) 
    nums.append(num)
prom = sum(nums) / len(nums)
print (f"El promedio de los números es {prom:.2f}")

# Complejidad Big O: O(n)
# Justificación: Porque recorre n elementos uno por uno para ingresar los números en la lista. Igualmente, recorre cada elemento con sum() para sumarlos.