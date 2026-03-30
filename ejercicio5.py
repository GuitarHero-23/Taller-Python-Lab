while True: 
    try: 
        num_entero = int(input("Ingrese un valor entero positivo"))
        if num_entero > 0: 
            break
        else: 
            print("Ingresar un valor que sea positivo")
    except ValueError: 
        print("El valor debe ser un numero entero")

contador = 0
while num_entero > 1: 
    print (f"{num_entero} / 2 = {num_entero//2}")
    num_entero = num_entero // 2
    contador += 1

print (f"Se dividió {contador} veces")

#Complejidad: O(log n)
#Justificacion: Es logaritmica porque cada iteracion el numero se divide para 2, lo que reduce el tamaño del problema por la mitad. 