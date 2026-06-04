### Clase del lunes 01/06

import streamlit as st

# Ingreso de Título en Cuerpo
st.title("Proyecto Final Diploma Business Analyst")

# Título en Barra lateral
st.sidebar.title("Parámetros")

# Leer imágenes

# st.image("logo_python.png") # tamaño por defecto
st.image("logo_python.png", width = 500)

# st.sidebar.image("logo_dmc.png") # tamaño por defecto
st.sidebar.image("logo_dmc.png", width = 100)

st.write("Elaborado por: Diana Córdova")

### Clase del miércoles 03/06

archivo = st.file_uploader("Cargue el archivo Excel o CSV")
