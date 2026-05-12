# Fundamentos de Data Science – Práctica para el Examen

# Contexto

# La tarea es limpiar y explorar los datos para una compañía de tecnología emergente que desarrolla aplicaciones móviles. La empresa quiere mejorar la experiencia del usuario y aumentar la retención de usuarios en sus aplicaciones. Han recolectado datos sobre el uso de sus aplicaciones y quieren entender mejor cómo los usuarios interactúan con sus productos.



# Requisitos

# 1) Limpieza de Datos:

# El primer paso en este proceso es usar Python para limpiar los datos y dejarlos listos para el análisis. Deben:

# Identificar y abordar cualquier valor duplicado.
# Identificar y abordar cualquier dato que falte en este conjunto de datos. Trátenlos de forma adecuada. Incluyan una breve descripción en el método que usan para tratar con los valores que faltan junto con una justificación para el uso de ese método.
# Asegurarse de que todas las columnas coincidan con los tipos de datos enumerados en el diccionario de datos.
# Identificar y abordar cualquier inconsistencia en los valores categóricos (ejemplo: android, Android, ANDROID).
# Identificar y abordar cualquier punto de datos inapropiados o inusuales (ejemplo: tiempo de uso de 10000 horas en una semana).


# 2) Exploración de Datos:

# El siguiente paso es completar una exploración de los datos usando Python. Esto debe incluir:

# Dos tipos diferentes de visualizaciones exploratorias univariantes. Cada visualización debe incluir una breve interpretación dentro del archivo de código.
# Dos tipos diferentes de visualizaciones exploratorias multivariantes. Cada visualización debe incluir una breve interpretación dentro del archivo de código.


# Diccionario de Datos

# user_id: Identificación única del usuario.
# app_version: Versión de la aplicación usada.
# platform: Plataforma del dispositivo (Android, iOS).
# session_duration: Duración de la sesión en minutos.
# number_of_sessions: Número de sesiones en un día.
# country: País del usuario.
# user_feedback: Puntuación de la experiencia del usuario (1-5).

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# # Configuramos la semilla para reproducibilidad
# np.random.seed(42)

# # Generamos los datos sintéticos
# user_id = range(1, 301)
# app_version = np.random.choice(['1.0', '1.1', '1.2', '1.3'], 300)
# platform = np.random.choice(['Android', 'iOS'], 300)
# session_duration = np.random.randint(1, 180, 300)
# number_of_sessions = np.random.randint(1, 20, 300)
# country = np.random.choice(['USA', 'Canada', 'Mexico', 'UK', 'Germany', 'France', 'Spain', 'Italy'], 300)
# user_feedback = np.random.randint(1, 6, 300)

# # Creamos el DataFrame
# data = pd.DataFrame({
#     'user_id': user_id,
#     'app_version': app_version,
#     'platform': platform,
#     'session_duration': session_duration,
#     'number_of_sessions': number_of_sessions,
#     'country': country,
#     'user_feedback': user_feedback
# })





# # Guardamos los datos en un archivo CSV
# data.to_csv('user_app_data.csv', index=False)
# print("Datos generados y guardados en 'user_app_data.csv'")

df = pd.read_csv('user_app_data.csv')
print("df : ",df)

# mostrar los primeros 10 registros
print(" primeros 10 registros : \n",df.head(10))

# los ultimos 5 registros
print("ultimos 5 registros : \n",df.tail())

# informacion general del dataframe:
print("informacion general del dataframe : \n",df.info())

# informacion estadisticas del dataframe :
print("informacion estadisticas del dataframe : \n",df.describe())

#----------------------------------------------------------------------------------------------

# 1) Limpieza de Datos:

# ---- El primer paso en este proceso es usar Python para limpiar los datos y dejarlos listos para el análisis. Deben: -------

# - Identificar y abordar cualquier valor duplicado.
print("Duplicados totales:", df.duplicated().sum())
# R: no se encuentran valores duplicados si se encuentran se debe realizar los siguientes comandos
# df = df.drop_duplicates()
# print("Duplicados totales despues del drop :", df.duplicated().sum())


# - Identificar y abordar cualquier dato que falte en este conjunto de datos. Trátenlos de forma adecuada.
#   Incluyan una breve descripción en el método que usan para tratar con los valores que faltan junto con una justificación 
#   para el uso de ese método.

        # verificar datos nulos en el dataframe
print("\nDatos nulos por columna : \n")
print(df.isnull().sum())


# - Asegurarse de que todas las columnas coincidan con los tipos de datos enumerados en el diccionario de datos.
 

# transformamos a los tipos correctos cada columna deacuerdo al diccionario de datos
df = df.astype({
    'app_version': 'float64',
    'platform': 'str',
    'session_duration': 'int64',
    'number_of_sessions': 'int64',
    'country': 'str',
    'user_feedback': 'int64'
})

   # ver tipos de datos en columnas
print("tipos de datos : ",df.dtypes)

# - Identificar y abordar cualquier inconsistencia en los valores categóricos 
# (ejemplo: android, Android, ANDROID).
print("\nIdentificar y abordar cualquier inconsistencia en los valores categóricos\n")
for col in df.columns:
    valores_unicos = df[col].unique()
    print(f"• {col:20} -> {len(valores_unicos)} únicos")
    print(f"  Lista de Valores :   {valores_unicos}\n")

# no se encuentran inconsistencias en los valores categoricos


# - Identificar y abordar cualquier punto de datos inapropiados o inusuales 
# (ejemplo: tiempo de uso de 10000 horas en una semana).
print(df)


#no se encuentra datos inapropiados o incorrectos salvo la columna session_duration donde si el dato que se entrega 
# no fuera en minutos el usuario tendria una coneccion muy alta que no seria real
# EJ("si un usuario tiene una duracion de session de 164 hrs y cantidad de session de 19
# entonces tendra 3116 horas equivalen a más de 4 meses de uso ininterrumpido (24/7).")


#2) Exploración de Datos:

# El siguiente paso es completar una exploración de los datos usando Python. Esto debe incluir:

# Dos tipos diferentes de visualizaciones exploratorias univariantes. Cada visualización debe incluir una breve interpretación dentro del archivo de código.



df = pd.read_csv('user_app_data.csv')
df['total_duration'] = df['session_duration'] * df['number_of_sessions']

plt.figure(figsize=(10, 6))
plt.hist(df['session_duration'], bins=25, color='skyblue', edgecolor='black', alpha=0.8)
plt.title('Distribución de Duración de Sesiones Individuales', fontsize=14)
plt.xlabel('Duración por Sesión')
plt.ylabel('Número de Usuarios')
plt.grid(True, alpha=0.3)

# Interpretación incluida en el gráfico:
plt.figtext(0.5, -0.12, 
            'Interpretación: La duración de las sesiones se distribuye de forma bastante uniforme\n'
            'entre 0 y 180 unidades, sin picos extremos. Sugiere un uso variado entre usuarios.', 
            ha='center', fontsize=10, bbox=dict(facecolor='lightblue', alpha=0.3))

plt.tight_layout()
plt.show()

# Dos tipos diferentes de visualizaciones exploratorias multivariantes. Cada visualización debe incluir una breve interpretación dentro del archivo de código.
 

