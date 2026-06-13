# Librería Streamlit para Crear la Aplicación Web
import streamlit as st

# Librería Pandas para Leer Archivos CSV y Excel
import pandas as pd

# Título Principal de la Aplicación
st.title("Proyecto Diploma Business Analyst")

# Título en Barra Lateral
st.sidebar.title("Parámetros")

# Imagen en la Página Principal de ancho específicado
st.image("logo_python.png", width = 500)

# Imagen en la Barra Lateral de ancho específicado
st.sidebar.image("logo_dmc.png", width = 100)

# Texto para visualizar el Autor del Proyecto
st.write("Elaborado por: Diana Córdova")

modulos = st.selectbox("Seleccione un Módulo", ["Home", "Carga y Perfil del Dataset", "Procesamiento de Datos", "Análisis visual"])


# Permite la carga de un archivo por parte del usuario
archivo = st.file_uploader("Cargue el archivo Excel o CSV")

# Valida si el usuario carga un archivo
if archivo is not None :

  # Valida si el archivo cargado tiene extensión .csv
  if archivo.name.endswith(".csv"):

    # Lee el archivo CSV y lo guarda en un DataFrame
    data = pd.read_csv(archivo)
    
    # Muestra el DataFrame en la aplicación
    st.write(data)

  # Valida si el archivo cargado tiene extensión .xlsx
  elif archivo.name.endswith(".xlsx"):

    # Lee el archivo Excel y lo guarda en un DataFrame
    data = pd.read_excel(archivo)
    
    # Muestra el DataFrame en la aplicación
    st.write(data)

  # Si el archivo no es CSV ni Excel, mostramos un mensaje de error
  else:
    st.write("Formato no válido")

# Si el usuario no ha cargado ningún archivo, mostramos un mensaje
else :
  st.write("Por favor cargue su archivo")

