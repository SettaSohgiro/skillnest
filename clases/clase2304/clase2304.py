
# alumnos = ["Ana", "Luis", "María"]

 

# alumnos.append("Carlos")       # agrega al final

# alumnos.insert(1, "Sofía")     # inserta en posición 1

# alumnos.remove("Luis")         # elimina por valor

# alumnos.sort()                 # ordena in-place (modifica la lista)

 

# print(alumnos)

# print(f"Total alumnos: {len(alumnos)}")

 

# # Verificar pertenencia — MUY eficiente

# print("Ana" in alumnos)        # True

# print("Pedro" in alumnos)      # False

 

# # List comprehension — la forma pythónica

# notas = [6.8, 4.2, 5.5, 7.0, 3.8, 6.1]

# aprobados = [n for n in notas if n >= 4.0]

# print(f"\nAprobados: {aprobados}")

# print(f"Reprobados: {len(notas) - len(aprobados)}")


# input_nombre = input("Ingrese su nombre: ")
# alumnos.append(input_nombre)

# for a in alumnos :
#     if a != "Ana":
#         print("alumnos: ", a) 
#     else:
#         print("alumnos: ", a, " ya no es  estudiante")


#limpieza de de string a listas
strin = " juan perez , santiago , CHILE   " 

limpieza = strin.strip()

print(limpieza)



#ejecicio ventas

ventas = {"Arica": 4500_000, "Valdivia": 3200000, "Santiago": 6100_000, "Chillan": 2800000}

# 1. Imprime cada región y su venta formateada con `$` y separador de miles
for region, venta in ventas.items():
    print(f"{region}: ${venta:,.2f}")


# 2. Calcula e imprime el **total** y el **promedio**
total_ventas = sum(ventas.values())
promedio_ventas = total_ventas / len(ventas)

print(f"Total ventas: ${total_ventas:,.2f}")
print(f"Promedio ventas: ${promedio_ventas:,.2f}")

# 3. Imprime qué región vendió más  
max_region = max(ventas, key=ventas.get)
print(f"Región con más ventas: {max_region}")



###  Mini-ejercicio 3 — Clasificador de temperatura

#Dado un valor de temperatura (en °C), clasifícalo como:

# - < 0°C → `"Bajo cero "`

# - 0–15°C → `"Frío "`  

# - 16–25°C → `"Templado "`

# - 26–35°C → `"Caluroso "`

# - > 35°C → `"Extremo "`

 

# Además, imprime si es adecuado para practicar deporte al aire libre (10–28°C).
temperatura = float(input("Ingrese la temperatura en °C: "))
if temperatura < 0:
    clasificacion = "Bajo cero"
elif 0 <= temperatura <= 15:
    clasificacion = "Frío"
elif 16 <= temperatura <= 25:
    clasificacion = "Templado"
elif 26 <= temperatura <= 35:
    clasificacion = "Caluroso"
else:
    clasificacion = "Extremo"

print(f"Clasificación: {clasificacion}")

if 10 <= temperatura <= 28:
    print("Es adecuado para practicar deporte al aire libre.")
else:
    print("No es adecuado para practicar deporte al aire libre.")