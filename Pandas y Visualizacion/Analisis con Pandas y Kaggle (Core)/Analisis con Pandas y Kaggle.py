# 1.- Preparación del Entorno
    # Asegúrate de tener instalado Pandas en tu entorno de trabajo.
    # Descarga el archivo dataset.csv desde Kaggle. Elige un dataset que te interese y que no incluya 
    # visualización de datos. Algunas sugerencias pueden ser datasets relacionados con ventas, compras, productos, etc.

import pandas as pd

# 2.- Cargar los Datos
    
    #Carga el archivo CSV en un DataFrame de Pandas.
df = pd.read_csv('data/retail_ferreteria.csv')
print("df",df)

    #Muestra las primeras 10 filas del DataFrame para confirmar que los datos se han cargado correctamente.
print(df.head(10))

#3.- Exploración Inicial de los Datos

    # Muestra las últimas 5 filas del DataFrame.
print(df.tail())    
    # Utiliza el método info() para obtener información general sobre el DataFrame, incluyendo el número de entradas, nombres de las columnas, tipos de datos y memoria utilizada.
print(df.info())
    
    # Genera estadísticas descriptivas del DataFrame utilizando el método describe().
print(df.describe())

#4.- Limpieza de Datos
    # Identifica y maneja los datos faltantes utilizando técnicas apropiadas 
    # (relleno con valores estadísticos, interpolación, eliminación, etc.).

        # verificar datos nulos en el dataframe
print("\nDatos nulos por columna : \n")
print(df.isnull().sum())

        # Rellenar valores nulos con interpolación
df['cantidad'] = df['cantidad'].interpolate()
df['precio_unitario'] = df['precio_unitario'].interpolate()

        #rellenar valores nulos con un valor específico
df['medio_pago'] = df['medio_pago'].fillna('Sin datos')
df['promo_producto'] = df['promo_producto'].fillna('Sin datos')
df['promo_pago'] = df['promo_pago'].fillna('Sin datos')
df['otros_productos'] = df['otros_productos'].fillna('Sin datos')


    #Corrige los tipos de datos si es necesario (por ejemplo, convertir cadenas a fechas).
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])           # Convertir a datetime
    
# print("df",df)
# print("tipos de datos : \n",df.dtypes)
# print(df.isnull().sum())

    #Elimina duplicados si los hay.
    
        # ver si contiane duplicados
print("Duplicados totales:", df.duplicated().sum())
        # eliminar duplicasdos
df = df.drop_duplicates()
print("Duplicados totales despues del drop :", df.duplicated().sum())

#5.- Transformación de Datos
# Crea nuevas columnas basadas en operaciones con las columnas existentes (por ejemplo, calcular ingresos a partir de ventas y precios).

# Calcular el ingreso total por venta
df['Ingreso'] = df.apply(lambda row: row['cantidad'] * row['precio_unitario'], axis=1)
print("df['Ingreso']",df['Ingreso'])
print("tipos de datos : \n",df.dtypes)

# Normaliza o estandariza columnas si es necesario. que los datos dentro la columna tengan el mismo formato como ejemplo "chile" y no "Chile" o "CHILE".

print("df.unique()->medio_pago",df['medio_pago'].unique())

df['medio_pago'] = df['medio_pago'].str.strip().str.lower()


reemplazo = {
    'mp': 'mercadopago',

}

df['medio_pago'] = df['medio_pago'].replace(reemplazo)

print("df.unique()->medio_pago",df['medio_pago'].unique())


# Clasifica los datos en categorías relevantes 
    # clasificacion del medio de pago y se agregara en la columna  tipo_pago donde ae agregan dos  tipos de datos efectivo o tarjeta
df['tipo_pago'] = df['medio_pago'].apply(lambda x: 'efectivo' if x == 'efectivo' else 'tarjeta')


#6.- Análisis de Datos
# Realiza agrupaciones de datos utilizando groupby para obtener insights específicos (por ejemplo, ventas por producto, ventas por región, etc.).

    # ventas por sucursales por articulos
df['mes_venta'] = df['fecha_hora'].dt.month
df['anio_venta'] = df['fecha_hora'].dt.year
print("df",df)
group_x_sucart = df.groupby(['sucursal', 'anio_venta','mes_venta'])

# Suma y promedio de ventas por producto y mes
ventas_por_producto_y_mes = group_x_sucart['total_venta'].agg(['sum', 'mean'])
    
print("ventas_por_producto_y_mes",ventas_por_producto_y_mes)

# Aplica funciones de agregación como sum, mean, count, min, max, std, y var.

    # Suma de ventas por sucursal
ventas_sucursal = df.groupby('sucursal')['total_venta'].sum()
print("ventas_sucursal : \n",ventas_sucursal)

    # Promedio de ventas por sucursal
promedio_ventas_sucursal = df.groupby('sucursal')['total_venta'].mean()
print("promedio_ventas_sucursal : \n",promedio_ventas_sucursal)

    # Número de ventas por sucursal
conteo_ventas_sucursal = df.groupby('sucursal')['total_venta'].count()
print("conteo_ventas_sucursal : \n",conteo_ventas_sucursal)

    # Ventas mínimas y máximas por sucursal
ventas_minimas_por_sucursal = df.groupby('sucursal')['total_venta'].min()
ventas_maximas_por_sucursal = df.groupby('sucursal')['total_venta'].max()
print("ventas_minimas_por_sucursal : \n",ventas_minimas_por_sucursal)
print("ventas_maximas_por_sucursal \n",ventas_maximas_por_sucursal)

# Desviación estándar de las ventas por sucursal
desviacion_estandar_ventas = df.groupby('sucursal')['total_venta'].std()
print(desviacion_estandar_ventas)

# Varianza de las ventas por sucursal
varianza_ventas = df.groupby('sucursal')['total_venta'].var().round(2)
print(varianza_ventas)

# Utiliza el método apply para realizar operaciones más complejas y personalizadas.
