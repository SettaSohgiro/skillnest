import pandas as pd

df = pd.read_csv('data/retail_ferreteria.csv')

## Cargar los Datos

# ver las primeras filas del dataframe
print(df.head(10))

## Exploración Inicial de los Datos

# ver las ultimas 5 filas del dataframe
print(df.tail())

# informacion general del dataframe
print(df.info())

# estadisticas descriptivas del dataframe
print(df.describe())

##  Inspección de los Datos

#tipo de datos de cada columna
print("Tipos de datos de cada columna:")
print(df.dtypes)

#contar valores unicos en columna Producto
print("Valores únicos en la columna 'producto':")
print(df['producto'].value_counts())

# valores únicos en la columna Tienda utilizando el método unique().
print("Valores únicos en la columna 'sucursal':")
print(df['sucursal'].unique())

## Filtrado de Datos

# Filtra el DataFrame para mostrar solo las filas donde las ventas (Ventas) sean mayores a 50.
print("Filas donde las ventas son mayores a 50:")
print(df[df['total_venta'] > 5000])    

# Filtra el DataFrame para mostrar solo las filas donde el precio (Precio) sea menor a 0.5.
print("Filas donde el precio_unitario es menor a 500:")
print(df[df['precio_unitario'] < 5000])

# Utilizando el método query(), filtra el DataFrame para mostrar las filas donde el producto sea Tornillos y las ventas sean mayores a 30.
print("Filas donde el producto es 'Destornillador' y las ventas son mayores a 30:")
# print(df['producto'].unique())
print(df.query("producto == 'Destornillador' and total_venta > 5000"))

## Slicing de Datos

# Selecciona y muestra solo las columnas producto y total_venta del DataFrame.
print("\nSelecciona y muestra solo las columnas Producto y Ventas del DataFrame:")
slicing_fc = df[['producto', 'total_venta']]
print(slicing_fc)

# Utilizando loc[], selecciona y muestra las filas de la 5 a la 10 (inclusive) y las columnas producto y sucursal.

print("\nSlicing de datos utilizando loc[] para filas 5 a 10 y columnas producto y sucursal:")
slicing_loc = df.loc[5:10, ['producto', 'sucursal']]
print(slicing_loc)


# Utilizando iloc[], selecciona y muestra las primeras 5 filas y las primeras 3 columnas del DataFrame.
print("\nSlicing de datos utilizando iloc[] para primeras 5 filas y primeras 3 columnas:")
slicing_iloc = df.iloc[0:5, 0:3]    
print(slicing_iloc)