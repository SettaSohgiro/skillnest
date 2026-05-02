print(6//5)

print(6/5)


a = 10
b = 5
potencia = a ** b
print("a elevado a la potencia de b es:", potencia)

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    if i < 10:    
        print("\nSiguiente tabla...\n")


#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. 
contraseña = "123"
while True:
    entrada_usuario = input("Introduce la contraseña: ")
    if entrada_usuario == contraseña:
        print("¡Contraseña correcta! Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    entrada_usuario = input("Introduce algo (escribe 'salir' para terminar): ")
    if entrada_usuario.lower() == "salir":
        print("¡Hasta luego!")
        break
    else:
        print(f"Eco: {entrada_usuario}")