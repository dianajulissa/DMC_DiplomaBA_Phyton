### Clase del lunes 01/06

# Importamos Streamlit para crear la aplicación web
import streamlit as st

# Importamos Pandas para leer archivos CSV y Excel
import pandas as pd

# Ingreso de Título Principal de la Aplicacion
st.title("Proyecto Diploma Business Analyst")

# Ingreso de Título en Barra Lateral
st.sidebar.title("Parámetros")

# Mostrando una imagen en la Página Principal
# st.image("logo_python.png") # tamaño por defecto

# Mostrando una imagen en la Página Principal con un ancho de 500 pixeles
st.image("logo_python.png", width = 500)

# Mostrando una imagen en la Barra Lateral
# st.sidebar.image("logo_dmc.png") # tamaño por defecto

# Mostrando una imagen en la Barra Lateral con un ancho de 100 pixeles
st.sidebar.image("logo_dmc.png", width = 100)

# Mostrando un texto con el Autor del Proyecto
st.write("Elaborado por: Diana Córdova")


### Clase del miércoles 03/06

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

