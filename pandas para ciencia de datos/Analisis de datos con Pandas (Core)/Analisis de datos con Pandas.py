import pandas as pd

##  Cargar los Datos
df = pd.read_csv('data/vgsales.csv')

# Ver las primeras y últimas filas del DataFrame
print("\nPrimeras filas del DataFrame:")
print(df.head(10))

##  Exploración Inicial de los Datos

print("\nÚltimas filas del DataFrame:")
print(df.tail())

# Obtener información general sobre el DataFrame
print("\nInformación del DataFrame:")
print(df.info())

# Generar estadísticas descriptivas
print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())


##  Inspección de los Datos

# Inspeccionar los tipos de datos de las columnas
print("\nTipos de datos de las columnas:")
print(df.dtypes)

#cuanta valores únicos hay en la columna 'Genre' con value_counts()
print("\nValores únicos en la columna 'Genre':")    
print(df['Genre'].value_counts())

#valores unicos en la columnan 'Platform' con unique()
print("\nValores únicos en la columna 'Platform':")
print(df['Platform'].unique())

##  Filtrado de Datos

# Filtra el dataframe donde las ventas de america del norte (NA_Sales) sean mayores a 1 millón
print("\nFiltrado de datos donde NA_Sales > 1 millón:")
filtrado = df[df['NA_Sales'] > 1]
print(filtrado)

# Filtra el dataframe donde las ventas de japon (JP_Sales) sean menores  a 0,1 millón
print("\nFiltrado de datos donde JP_Sales < 0,1 millón:")
filtrado_jp = df[df['JP_Sales'] < 0.1]
print(filtrado_jp)

#Utilizando el método query(), filtra el DataFrame para mostrar las filas donde el género sea Action y las ventas globales (Global_Sales) sean mayores a 2 millones.
print("\nFiltrado de datos utilizando query() para género Action y Global_Sales > 2 millones:")
filtrado_query = df.query("Genre == 'Action' and Global_Sales > 2")
print(filtrado_query)

## Slicing de Datos

# Selecciona y muestra solo las columnas Name y Global_Sales del DataFrame.
print("\nSlicing de datos para columnas Name y Global_Sales:")
slicing_fc = df[['Name', 'Global_Sales']]
print(slicing_fc)

# Utilizando loc[], selecciona y muestra las filas de la 5 a la 10 (inclusive) y las columnas Name y Genre.

print("\nSlicing de datos utilizando loc[] para filas 5 a 10 y columnas Name y Genre:")
slicing_loc = df.loc[5:10, ['Name', 'Genre']]
print(slicing_loc)


# Utilizando iloc[], selecciona y muestra las primeras 5 filas y las primeras 3 columnas del DataFrame.
print("\nSlicing de datos utilizando iloc[] para primeras 5 filas y primeras 3 columnas:")
slicing_iloc = df.iloc[0:5, 0:3]    
print(slicing_iloc)