verso1 = ['dale', 'a', 'tu', 'cuerpo']
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)

# Lista de temperaturas diarias
temperaturas = [22.5, 21.0, 23.3, 25.2, 24.5]
media_temperatura = sum(temperaturas) / len(temperaturas)
print("Temperatura media:", media_temperatura)


# tuplas
# Coordenadas geográficas de una ubicación
coordenadas = (19.4326, -99.1332)  # Latitud y longitud de Ciudad de México

def calcular_distancia(coord1, coord2):
    # Implementación ficticia para calcular la distancia
    distancia = 10  # Solo un valor de ejemplo
    return distancia

distancia = calcular_distancia(coordenadas, (34.0522, -118.2437))
print("Distancia:", distancia)

# Diccionario con información sobre un conjunto de datos
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Número de filas:", dataset_info["filas"])

for i in range(4):
   print(i)

#Range con 2 argumentos
print("Range con 2 argumentos:")

for x in range(2, 8):
   print(x)

#Range con 3 argumentos
print("Range con 3 argumentos:")
#inicio = 2, fin = 10, paso = 3
for i in range(2, 10, 3):
   print(i)

#Imprime: 'P', 'y', 't', 'h', 'o', 'n'
print("Iterando sobre cada letra de 'Python':")

for letra in 'Python':
   print(letra)


#Imprime: 'P', 'y', 't', 'h', 'o', 'n'

tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
   print(i, tupla[i])
#Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
   print(fruta)
#Imprime: fresa, manzana, cereza


