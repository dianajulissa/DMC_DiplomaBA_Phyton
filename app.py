###########################################################################################################################################

# Librería Streamlit para Crear la Aplicación Web
import streamlit as st

# Librería Pandas para Leer Archivos CSV y Excel
import pandas as pd

###########################################################################################################################################

# Título Principal de la Aplicación
st.title("Diploma Business Analyst")

# Título en Barra Lateral
st.sidebar.title("Parámetros")

# Imagen en la Página Principal de ancho específicado
st.image("logo_python.png", width = 500)

# Imagen en la Barra Lateral de ancho específicado
st.sidebar.image("logo_dmc.png", width = 100)

# Texto para visualizar el Autor del Proyecto
st.write("Elaborado por: Diana Córdova")


# Despliega un Menú de Opciones en la Barra Lateral
modulos = st.sidebar.selectbox("Seleccione un Módulo", ["Home", "Carga y Perfil del Dataset", "Procesamiento de Datos", "Análisis Visual"])

###########################################################################################################################################

if modulos == "Home":

    st.write("Bienvenido a la Aplicación")
    st.write("Elaborado por: Diana Córdova")

    #if st.session_state.data is not None:
    #    st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
    #else:
    #    st.info("Aún no se ha cargado ningún dataset.")

###########################################################################################################################################

elif modulos == "Carga y Perfil del Dataset":
    
    st.write("Carga y Perfil del Dataset")
    
    # Permite la carga de un archivo por parte del usuario
    archivo = st.file_uploader("Cargue el archivo Excel o CSV")

    # Valida la Carga de un Archivo
    if archivo is not None :

        # Verificando que el archivo cargado tiene extensión .csv
        if archivo.name.endswith(".csv"):
            
            # Lee el archivo CSV y lo guarda en un DataFrame
            data = pd.read_csv(archivo)
            
            # Muestra el DataFrame en la aplicación
            st.write(data)
            
        # Verificando que el archivo cargado tiene extensión .xlsx
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

###########################################################################################################################################

elif modulos == "Procesamiento de Datos":
  st.write("Procesamiento de Datos")

###########################################################################################################################################

elif modulos == "Análisis Visual":
  st.write("Análisis Visual")

###########################################################################################################################################




###########################################################################################################################################
