###########################################################################################################################################

# Librería Streamlit para Crear la Aplicación Web
import streamlit as st

# Librería Pandas para Leer Archivos CSV y Excel
import pandas as pd

###########################################################################################################################################

# Almacenamiento del Dataset Cargado
if "data" not in st.session_state:
    st.session_state.data = None

# Almacenamiento del Nombre del Archivo Cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None
    
###########################################################################################################################################

# Título Principal de la Aplicación
st.title("Diploma Business Analyst - Python")

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

    # Validando la Carga del Dataset
    if st.session_state.data is not None:
        st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
        
    else:
        st.info("Aún no se ha cargado ningún dataset.")

###########################################################################################################################################

elif modulos == "Carga y Perfil del Dataset":
    
    st.write("Carga y Perfil del Dataset")
    
    # Permite la carga de un archivo por parte del usuario
    archivo = st.file_uploader("Cargue el archivo Excel o CSV")

    # Valida la Carga de un Archivo
    if archivo is not None :

        # Guardamos el nombre del archivo en session_state
        st.session_state.nombre_archivo = archivo.name

        # Verificando que el archivo cargado tiene extensión .csv
        if archivo.name.endswith(".csv"):
            
            # Lee el archivo CSV y lo guarda en un session_state
            st.session_state.data = pd.read_csv(archivo)
            
            # Muestra el DataFrame en la aplicación
            #st.write(data)
            
        # Verificando que el archivo cargado tiene extensión .xlsx
        elif archivo.name.endswith(".xlsx"):
            
            # Lee el archivo Excel y lo guarda en un session_state
            st.session_state.data = pd.read_excel(archivo)
            
            # Muestra el DataFrame en la aplicación
            #st.write(data)
            
        # Si el archivo no es CSV ni Excel, mostramos un mensaje de error
        else:
            
            st.write("Formato no válido")
        
    # Confirmamos que el archivo fue cargado
    st.success("Archivo cargado correctamente")
        
    # Si ya existe un dataset cargado, lo mostramos
    if st.session_state.data is not None:

        st.write(f"Archivo actual: **{st.session_state.nombre_archivo}**")

        st.subheader("Vista previa del dataset")
        st.dataframe(st.session_state.data)

        st.subheader("Perfil básico del dataset")

        # Número de filas y columnas
        st.write("Filas:", st.session_state.data.shape[0])
        st.write("Columnas:", st.session_state.data.shape[1])

        # Nombres de columnas
        st.write("Columnas del dataset:")
        st.write(st.session_state.data.columns.tolist())

        # Tipos de datos
        st.write("Tipos de datos:")
        st.write(st.session_state.data.dtypes)

        # Valores nulos
        st.write("Valores nulos por columna:")
        st.write(st.session_state.data.isnull().sum())

        # Estadística descriptiva
        st.write("Estadística descriptiva:")
        st.write(st.session_state.data.describe())

        # Botón para eliminar el dataset cargado
        if st.button("Eliminar dataset cargado"):
            st.session_state.data = None
            st.session_state.nombre_archivo = None
            st.rerun()
    
    # Si el usuario no ha cargado ningún archivo, mostramos un mensaje
    else :
        st.write("Por favor cargue su archivo")

###########################################################################################################################################

elif modulos == "Procesamiento de Datos":
    
    st.subheader("Procesamiento de Datos")

    if st.session_state.data is not None:
    
        data = st.session_state.data

        st.write("Dataset disponible para procesamiento:")
        st.dataframe(data)

        st.write("Valores nulos por columna:")
        st.write(data.isnull().sum())
        
    else:
        st.warning(
            "Primero debe cargar un dataset en el módulo "
            "'Carga y Perfil del Dataset'."
        )

###########################################################################################################################################

elif modulos == "Análisis Visual":
  st.write("Análisis Visual")

###########################################################################################################################################




###########################################################################################################################################
