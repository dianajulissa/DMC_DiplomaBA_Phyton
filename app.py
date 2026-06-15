###########################################################################################################################################

# Librería Streamlit para Crear la Aplicación Web
import streamlit as st

# Librería Pandas para Leer Archivos CSV y Excel
import pandas as pd

# Librería para Cálculo Numérico y Análisis de Datos
import numpy as np

###########################################################################################################################################

# Almacenamiento del Dataset Cargado
if "data" not in st.session_state:
    st.session_state.data = None

# Almacenamiento del Nombre del Archivo Cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None
    
###########################################################################################################################################

# Título Principal de la Aplicación
st.title("Diploma Business Analyst")

# Título en Barra Lateral
st.sidebar.title("Parámetros")

# Imagen en la Página Principal de ancho específicado
st.image("logo_python.png", width = 200)

# Imagen en la Barra Lateral de ancho específicado
st.sidebar.image("logo_dmc.png", width = 100)

# Texto para visualizar el Autor del Proyecto
#st.write("Elaborado por: Diana Córdova")

###########################################################################################################################################

# Despliega un Menú de Opciones en la Barra Lateral
modulos = st.sidebar.selectbox("Seleccione un Módulo", 
                               ["Home", "Carga y Perfil del Dataset", "Procesamiento de Datos", "Análisis Visual"])

###########################################################################################################################################

if modulos == "Home":

    st.subheader("Presentación del Proyecto")
    
    st.write("**Objetivo**")
    st.write("""Construir una aplicación web en Streamlit capaz de procesar cualquiera de los cuatro datasets propuestos 
                y diferenciando 4 módulos: Home, Carga y Perfil del Dataset, Procesamiento de Datos y Análisis Visual 
                mediante gráficos interactivos.""")
    
    st.write("**Elaborado por**")
    st.write("Diana Córdova Rodríguez")
        
    st.write("**Descripción de Datasets**")
    
    st.write("***- AI_Impact_on_Jobs_2030.csv***: ", 
             "Mercado laboral e impacto de la inteligencia artificial en empleos, salarios, habilidades y demanda futura.")
    
    st.write("***- sample_-_superstore.csv***: ",
            "Ventas de una tienda: pedidos, clientes, regiones, categorías, ventas, descuentos y utilidad.")
    
    st.write("***- synthetic_ecommerce_order_risk_dataset.csv***: ",
            "Pedidos de e-commerce con variables de país, dispositivo, método de pago, valor de orden, entrega, devolución, fraude y etiqueta de riesgo.")
    
    st.write("***- Teen_Mental_Health_Dataset.csv***: ",
            "Hábitos digitales, sueño, actividad física, interacción social y variables de bienestar en adolescentes.")

    # Validando la Carga del Dataset
    if st.session_state.data is not None:
        st.success(f"Dataset Cargado: {st.session_state.nombre_archivo}")
        
    else:
        st.info("Aún no se ha cargado ningún dataset.  \n Diríjase al Módulo **Carga y Perfil del Dataset**")

###########################################################################################################################################

elif modulos == "Carga y Perfil del Dataset":
    
    st.subheader("Carga y Perfil del Dataset")
    
    # Permite la carga de un archivo por parte del usuario
    archivo = st.file_uploader("Seleccione el Dataset a cargar (archivo Excel o CSV)",
                              type = ["csv", "xlsx"]
                                  )

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

        #st.write(f"Archivo actual: **{st.session_state.nombre_archivo}**")
        st.write("**Archivo Cargado**")
        st.write(f"{st.session_state.nombre_archivo}")

        #st.subheader("Vista Previa del Dataset")
        st.write("**Vista Previa del Dataset**")
        st.dataframe(st.session_state.data)

        #st.subheader("Perfil Básico del Dataset")
        st.write("**Dimensiones del Dataset**")

        # Número de filas y columnas
        st.write("- Número de Filas:", st.session_state.data.shape[0])
        st.write("- Número de Columnas:", st.session_state.data.shape[1])

        # Nombres de columnas
        st.write("**Columnas del Dataset**")
        st.write(st.session_state.data.columns.tolist())

        # Tipos de datos
        #st.write("**Tipos de datos**")
        #st.write(st.session_state.data.dtypes)

        # Columnas y Tipo de Datos
        st.write("**Columnas y Tipos de datos**")
        df_info = pd.DataFrame({
                                    'Tipo de Dato'    : st.session_state.data.dtypes.astype(str),
                                    'Valores No Nulos': st.session_state.data.count(),
                                    'Valores Nulos'   : st.session_state.data.isnull().sum()
                                })
        st.write(df_info)
    
        # Valores Nulos
        #st.write("**Valores nulos por columna:**")
        #st.write(st.session_state.data.isnull().sum())

        # Estadística Descriptiva
        st.write("**Resumen Inicial - Estadística Descriptiva:**")
        st.write(st.session_state.data.describe())
        #st.write(st.session_state.data.describe(include='all'))

        # Botón para Eliminar el Dataset Cargado
        if st.button("Eliminar Dataset Cargado"):
            
            st.session_state.data           = None
            st.session_state.nombre_archivo = None
            st.rerun()
            st.write("Dataset eliminado")
    
    # Si el usuario no ha cargado ningún archivo, mostramos un mensaje
    else :
        #st.write("Por favor cargue su archivo")
        st.info("Aún no se ha cargado ningún dataset.  \n Diríjase al Módulo **Carga y Perfil del Dataset**")

###########################################################################################################################################

elif modulos == "Procesamiento de Datos":
    
    st.subheader("Procesamiento de Datos")

    if st.session_state.data is not None:
    
        data = st.session_state.data

        st.write("Dataset disponible para el procesamiento:")
        st.dataframe(data)

        #st.write("Valores nulos por columna:")
        #st.write(data.isnull().sum())
    
        # DETECCION DE VARIABLES: Numéricas, fechas, categóricas
        
        st.header("**Detección de variables**")
        
        # Conversión automática de las columnas de texto que parecen fechas
        for col in st.session_state.data.columns:
            
            st.write(col)
            st.write(st.session_state.data[col].dtype)
            
            if st.session_state.data[col].dtype == 'object':
            #if st.session_state.data[col].dtype == 'str':
                
                try:
                    st.write("entro")
                    # Verificación rápida si parece fecha antes de convertir
                    if st.session_state.data[col].astype(str).str.contains(r'\d{4}|\d{2}[-/]\d{2}').any():
                        st.write("entro2")
                        #st.write(pd.to_datetime(st.session_state.data[col]))
                        
                        st.session_state.data[col] = pd.to_datetime(st.session_state.data[col], errors='ignore')
                        #st.write(st.session_state.data[col])
                        #st.write(st.session_state.data)
                        st.write(st.session_state.data[col].dtype)
                
                except:
                    pass
                    
        st.dataframe(st.session_state.data)
        
        # Clasificar según el tipo de dato real
        num_cols  = st.session_state.data.select_dtypes(include=[np.number]).columns.tolist()
        date_cols = st.session_state.data.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()
        cat_cols  = st.session_state.data.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # Mostrar clasificación en columnas visuales
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("Variables Numéricas")
            st.write(num_cols if num_cols else "Ninguna")
            
        with c2:
            st.subheader("Variables Tipo Fecha")
            st.write(date_cols if date_cols else "Ninguna")
            
        with c3:
            st.subheader("Variables Categóricas")
            st.write(cat_cols if cat_cols else "Ninguna")
            
    else:
        st.warning(
            "Primero debe cargar un dataset.  \n"
            "Diríjase al Módulo **Carga y Perfil del Dataset**."
        )

###########################################################################################################################################

elif modulos == "Análisis Visual":
    
    st.subheader("Análisis Visual")

    if st.session_state.data is not None:
    
        data = st.session_state.data

        st.write("Dataset disponible para Análisis Visual:")
        st.dataframe(data)
    
        lista_columna_numerica   = data.select_dtypes(include = "number").columns.tolist()
        
        variable_numerica        = st.selectbox("Selecione la columna númerica", lista_columna_numerica)
        
        lista_columna_categorica = data.select_dtypes(include=["object", "category"]).columns.tolist()
        
        variable_categorica      = st.selectbox("Seleccione la columna categórica", lista_columna_categorica)
        
    else:
        st.warning(
            "Primero debe cargar un dataset.  \n"
            "Diríjase al Módulo **Carga y Perfil del Dataset**."
        )

###########################################################################################################################################




###########################################################################################################################################
