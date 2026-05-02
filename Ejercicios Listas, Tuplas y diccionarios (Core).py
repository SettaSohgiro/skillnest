
#Carga de Datos:
#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.
ventas = [
    {"fecha": "2024-01-01", "producto": "Camiseta", "cantidad": 2, "precio": 19.99},
    {"fecha": "2024-01-02", "producto": "Pantalón", "cantidad": 1, "precio": 39.99},
    {"fecha": "2024-01-03", "producto": "Zapatos", "cantidad": 1, "precio": 59.99}
]

#Cálculo de Ingresos Totales:
#Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
print(f"Ingresos totales: ${ingresos_totales:.2f}")


#Análisis del Producto Más Vendido:
#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(f"Producto más vendido: {producto_mas_vendido} con {ventas_por_producto[producto_mas_vendido]} unidades vendidas.")


#Promedio de Precio por Producto:
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio_total = venta["cantidad"] * venta["precio"]
    
    if producto in precios_por_producto:
        precios_por_producto[producto] = (precios_por_producto[producto][0] + precio_total, precios_por_producto[producto][1] + cantidad)
    else:
        precios_por_producto[producto] = (precio_total, cantidad)

# Imprimir el precio promedio de venta para cada producto
for producto, (suma_precios, cantidad_vendida) in precios_por_producto.items():
    precio_promedio = suma_precios / cantidad_vendida if cantidad_vendida > 0 else 0
    print(f"{producto}: ${precio_promedio:.2f}")


#Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingresos = venta["cantidad"] * venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos
    else:
        ingresos_por_dia[fecha] = ingresos


# Imprimir los ingresos totales por día
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: ${ingresos:.2f}")


#Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.
resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingresos = cantidad * venta["precio"]
    
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += ingresos
    else:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad,
            "ingresos_totales": ingresos,
            "precio_promedio": 0  # Se calculará después
        }

# Calcular el precio promedio para cada producto
for producto, datos in resumen_ventas.items():
    cantidad_total = datos["cantidad_total"]
    ingresos_totales = datos["ingresos_totales"]
    datos["precio_promedio"] = ingresos_totales / cantidad_total if cantidad_total > 0 else 0

# Imprimir el resumen de ventas
for producto, datos in resumen_ventas.items():
    print(f"{producto}:")
    print(f"  Cantidad total: {datos['cantidad_total']}")
    print(f"  Ingresos totales: ${datos['ingresos_totales']:.2f}")
    print(f"  Precio promedio: ${datos['precio_promedio']:.2f}")
