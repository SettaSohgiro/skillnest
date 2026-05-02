
#Ejercicio 1: Saludo Personalizado
nombre = input("Ingresa tu Nombre : ")
edad = int(input("Ingresa tu Edad : "))

print(f"Hola {nombre} me da gusto conocerte, veo que tienes {edad} años")

#Ejercicio 2: Manipulación de Cadenas

mi_nombre_completo = " Lientur agustin Quelempan valladares "
print(f"{mi_nombre_completo}".upper().strip()) 
print(f"{mi_nombre_completo}".lower().strip())
nombre = mi_nombre_completo.strip().split()[0]
print(f"La cantidad de letras de mi primer nombre es: {len(nombre)}.")

nombres_separados = mi_nombre_completo.strip().split()
#print(nombres_separados)
nombres_separados[0] = input("Ingrese su nuevo nombre : ")
mi_nombre_completo =  " ".join(nombres_separados)
print(f"Mi nuevo nombre completo es: { mi_nombre_completo.upper()}")


# Ejercicio 3: Lista de Nombres

lista_nombres = input("Ingresa una lista de nombres separados por comas : ")
nombres = lista_nombres.split(",")
for nombre in nombres:
    print(f"{nombre.strip()}")


