import pandas as pd
import numpy as np
#--Carga el archivo CSV en un DataFrame de Pandas.

df = pd.read_csv('data/retail_ferreteria.csv')
print("df",df)
print(df.head(10))
    # Muestra las últimas 5 filas del DataFrame.
print(df.tail())    
    # Utiliza el método info() para obtener información general sobre el DataFrame, incluyendo el número de entradas, nombres de las columnas, tipos de datos y memoria utilizada.
print(df.info())
    # Genera estadísticas descriptivas del DataFrame utilizando el método describe().
print(df.describe())
    # Inspección de los Datos
print(df.dtypes)


#1.- Transformación de Datos
# --Crea nuevas columnas: Basándonos en los datos existentes, crea nuevas columnas que sean útiles para el análisis. Por ejemplo, calcula el ingreso total por venta y normaliza las ventas.
    # se crea columna de ingreso total por venta de articulos.
df['ingreso_total'] = df['cantidad'] * df['precio_unitario']

# --Clasifica los datos: Crea una columna que clasifique las ventas en categorías significativas (e.g., ‘Alta’, ‘Media’, ‘Baja’).
    # se utiliza la columna de ingreso_total para clasificar las ventas de cada articulo con las categoria ‘Alta’, ‘Media’, ‘Baja’
df['Clasificación'] = df['ingreso_total'].apply(lambda x: 'Alta' if x > 50000 else 'Media' if x > 15000 else 'Baja')
print("df : ",df)
#2.- Agrupación y Agregación
# Agrupación por múltiples columnas: Realiza agrupaciones por categorías como producto y tienda, producto y mes, etc.
    # agrupamos para obtener productos vendidos en cada sucursal
group_x_sucpro = df.groupby(['sucursal', 'producto'])
# Suma y promedio de ventas por producto y mes
ventas_por_producto_y_mes = group_x_sucpro['total_venta'].agg(['sum', 'mean'])
    
print("ventas_por_producto_y_mes",ventas_por_producto_y_mes)
# Aplicar funciones de agregación: Utiliza funciones como sum, mean, count, min, max, std, y var para obtener estadísticas descriptivas de cada grupo.

    # Suma de ventas por sucursal
ventas_sucursal = df.groupby(['sucursal', 'producto'])['total_venta'].sum()
print("ventas_sucursal : \n",ventas_sucursal)


    # Promedio de ventas por sucursal
promedio_ventas_sucursal = df.groupby(['sucursal', 'producto'])['total_venta'].mean()
print("promedio_ventas_sucursal : \n",promedio_ventas_sucursal)

    # Número de ventas por sucursal
conteo_ventas_sucursal = df.groupby(['sucursal', 'producto'])['total_venta'].count()
print("conteo_ventas_sucursal : \n",conteo_ventas_sucursal)

    # Ventas mínimas y máximas por sucursal
ventas_minimas_por_sucursal = df.groupby(['sucursal', 'producto'])['total_venta'].min()
ventas_maximas_por_sucursal = df.groupby(['sucursal', 'producto'])['total_venta'].max()
print("ventas_minimas_por_sucursal : \n",ventas_minimas_por_sucursal)
print("ventas_maximas_por_sucursal \n",ventas_maximas_por_sucursal)

# Desviación estándar de las ventas por sucursal
desviacion_estandar_ventas = df.groupby(['sucursal', 'producto'])['total_venta'].std()
print(desviacion_estandar_ventas)

# Varianza de las ventas por sucursal
varianza_ventas = df.groupby(['sucursal', 'producto'])['total_venta'].var().round(2)

print(varianza_ventas)

#3.- Análisis Personalizado con apply
# --Función personalizada: Aplica funciones personalizadas para realizar análisis específicos que no se pueden lograr con las funciones de agregación estándar.
    # se clasifica el medio de pago si es en efectivo o con alguna tarjeta o atraves de la web
df['Clasificación_forma_compra'] = df['medio_pago'].apply(lambda x: 'efectivo' if x == "efectivo" else 'tarjeta' if x == "tarjeta_débito" else 'tarjeta' if x == "tarjeta_crédito" else 'web')
# --Ejemplo de uso avanzado: Calcula la desviación de cada venta respecto a la media de su grupo.
    # calculo la media de los producto
mean_A = df['total_venta'].mean()
# Calcular desviación usando .apply()

df['MAD_A'] = df['total_venta'].apply(lambda x: np.abs(x - mean_A))

print("df  : ",df)
#4.- Documentación
# --Comentarios claros: Documenta claramente cada paso del análisis, explicando qué se hizo y por qué se hizo.
# --Código legible: Asegúrate de que el código sea legible y esté bien comentado.
