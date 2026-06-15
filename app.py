###########################################################################################################################################
###########################################################################################################################################
# INICIO DE CODIGO
###########################################################################################################################################

###########################################################################################################################################
# LIBRERIAS
###########################################################################################################################################

# Librería Streamlit para Crear la Aplicación Web
import streamlit as st

# Librería Pandas para Leer Archivos CSV y Excel
import pandas as pd

# Librería para Cálculo Numérico y Análisis de Datos
import numpy as np

###########################################################################################################################################
# DATOS DE SESION
###########################################################################################################################################

# Almacenamiento del Dataset Cargado
if "data" not in st.session_state:
    st.session_state.data = None

# Almacenamiento del Nombre del Archivo Cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None
    
###########################################################################################################################################
# TITULO E IMAGENES DE APLICACION WEB
###########################################################################################################################################

# Título Principal de la Aplicación
st.title("Diploma Business Analyst")

# Título en Barra Lateral
st.sidebar.title("Parámetros")

# Imagen en la Página Principal de ancho específicado
st.image("logo_python.png", width = 150)

# Imagen en la Barra Lateral de ancho específicado
st.sidebar.image("logo_dmc.png", width = 80)

# Texto para visualizar el Autor del Proyecto
st.write("Elaborado por: Diana Córdova")

###########################################################################################################################################
# MENU DE OPCIONES EN BARRA LATERAL
###########################################################################################################################################

# Despliega un Menú de Opciones en la Barra Lateral
modulos = st.sidebar.selectbox("Seleccione un Módulo", 
                               ["Home", 
                                "Carga y Perfil del Dataset", 
                                "Procesamiento de Datos", 
                                "Análisis Visual"])

###########################################################################################################################################
# MODULO: HOME
###########################################################################################################################################

if modulos == "Home":

    # Título de Módulo
    st.subheader("Presentación del Proyecto")

    # Objetivo del Proyecto
    st.write("**Objetivo**")
    st.write("""Construir una aplicación web en Streamlit capaz de procesar cualquiera de los cuatro datasets propuestos 
                y diferenciando 4 módulos: Home, Carga y Perfil del Dataset, Procesamiento de Datos y Análisis Visual 
                mediante gráficos interactivos.""")

    # Autor del Proyecto
    st.write("**Elaborado por**")
    st.write("- Diana Córdova Rodríguez")

    # Descripción de Datasets
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
        st.success(f"✅ Dataset Cargado: {st.session_state.nombre_archivo}")
        
    else:
        st.info("""🚨 Aún no se ha cargado ningún dataset. Diríjase al Módulo **Carga y Perfil del Dataset**""")

###########################################################################################################################################
# MODULO: CARGA Y PERFIL DE DATOS
###########################################################################################################################################

elif modulos == "Carga y Perfil del Dataset":

    # Título de Módulo
    st.subheader("Carga y Perfil del Dataset")
    
    # Permite la carga de un archivo por parte del usuario sugiriendo el formato correcto
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
        st.success("✅ Archivo cargado correctamente")
        
    # Si ya existe un dataset cargado, lo mostramos
    if st.session_state.data is not None:

        #st.write(f"Archivo actual: **{st.session_state.nombre_archivo}**")
        #st.write("**Archivo Cargado**")
        #st.write(f"{st.session_state.nombre_archivo}")
        st.success(f"✅ Dataset Cargado:  \n {st.session_state.nombre_archivo}")

        #st.subheader("Vista Previa del Dataset 🔍")
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

        st.info("Diríjase al Módulo **Procesamiento de Datos** para procesar el dataset cargado.")
    
    # Si el usuario no ha cargado ningún archivo, mostramos un mensaje
    else :
        #st.write("Por favor cargue su archivo")
        st.info("🚨 Aún no se ha cargado ningún dataset. Diríjase al Módulo **Carga y Perfil del Dataset**.")

###########################################################################################################################################
# MODULO: PROCESAMIENTO DE DATOS
###########################################################################################################################################

elif modulos == "Procesamiento de Datos":

    # Título del Módulo
    st.subheader("Procesamiento de Datos")

    # Validando que la carga del dataset
    if st.session_state.data is not None:

        st.success(f"✅ Dataset Cargado:  \n {st.session_state.nombre_archivo}")
    
        data = st.session_state.data
        
        st.write("**Dataset inicial disponible para el procesamiento:**")
        st.dataframe(data)

        #st.write("Valores nulos por columna:")
        #st.write(data.isnull().sum())

        #----------------------------------------------------------------------------------------------------------------------------------
        # DETECCION DE TIPO DE VARIABLES
        #----------------------------------------------------------------------------------------------------------------------------------
        
        st.write("**Dataset luego de la detección de variables tipo Fecha**")
        
        # Conversión automática de las columnas de texto que parecen fechas
        for col in st.session_state.data.columns:
            
            if st.session_state.data[col].dtype == 'str':
                
                try:
                    # Limpiar espacios en blanco invisibles del string
                    col_limpia = st.session_state.data[col].astype(str).str.strip()
                    
                    # Expresión regular estricta: La celda debe EMPEZAR (^) y TERMINAR ($) con formato de fecha.
                    # Detecta: AAAA-MM-DD, DD-MM-AAAA, AAAA/MM/DD, DD/MM/AAAA (y permite celdas vacías o N/A aislados)
                    patron_fecha_estricto = r'^(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})$'
                    
                    # Validar que al menos un valor cumpla el patrón estricto
                    if col_limpia.str.contains(patron_fecha_estricto, regex=True).any():
                        # Validar también que la columna NO esté llena de texto largo (promedio de caracteres bajo)
                        # Esto evita falsos positivos si un texto casual coincide por error
                        if col_limpia.str.len().mean() < 15:
                            st.session_state.data[col] = pd.to_datetime(st.session_state.data[col], errors='coerce')
                
                except:
                    pass
                    
        st.dataframe(st.session_state.data)

        # Columnas y Tipo de Datos Convertidos
        st.write("**Columnas y Tipos de Datos después de Conversión**")
        df_info = pd.DataFrame({
                                    'Tipo de Dato'    : st.session_state.data.dtypes.astype(str),
                                    'Valores No Nulos': st.session_state.data.count(),
                                    'Valores Nulos'   : st.session_state.data.isnull().sum()
                                })
        st.write(df_info)
        
        # Clasificar según Tipo de Dato
        num_cols  = st.session_state.data.select_dtypes(include=[np.number]).columns.tolist()
        date_cols = st.session_state.data.select_dtypes(include=['datetime64', 'datetime']).columns.tolist()
        cat_cols  = st.session_state.data.select_dtypes(include=['object', 'category']).columns.tolist()

        # Variables Numéricas
        st.write("**Variables Numéricas**")
        st.write(num_cols if num_cols else "Ninguna")

        # Variables Tipo Fecha
        st.write("Variables Tipo Fecha")
        st.write(date_cols if date_cols else "Ninguna")

        # Variables Categóricas
        st.write("Variables Categóricas")
        st.write(cat_cols if cat_cols else "Ninguna")
        
        # Mostrar clasificación en columnas visuales
        #c1, c2, c3 = st.columns(3)
        #with c1:
        #    st.subheader("Variables Numéricas")
        #    st.write(num_cols if num_cols else "Ninguna")
        #    
        #with c2:
        #    st.subheader("Variables Tipo Fecha")
        #    st.write(date_cols if date_cols else "Ninguna")
        #    
        #with c3:
        #    st.subheader("Variables Categóricas")
        #    st.write(cat_cols if cat_cols else "Ninguna")

        #----------------------------------------------------------------------------------------------------------------------------------
        # VALIDANDO LA CALIDAD
        #----------------------------------------------------------------------------------------------------------------------------------
        
        #st.header("Diagnóstico de Calidad de Datos")
        st.write("**Diagnóstico de Calidad de Datos**")
        
        nulos_totales      = st.session_state.data.isnull().sum().sum()
        duplicados_totales = st.session_state.data.duplicated().sum()
        
        col_val1, col_val2 = st.columns(2)
        
        col_val1.metric("Valores Nulos Detectados", nulos_totales, delta=f"-{nulos_totales}" if nulos_totales > 0 else 0, delta_color="inverse")
        col_val2.metric("Filas Duplicadas", duplicados_totales, delta=f"-{duplicados_totales}" if duplicados_totales > 0 else 0, delta_color="inverse")
        
        # Detectar valores no válidos (ej: textos vacíos disfrazados de espacios o "N/A")
        valores_raros = 0
        
        if len(cat_cols) > 0:
            
            valores_raros = st.session_state.data[cat_cols].map(lambda x: str(x).strip().lower() in ['n/a', 'na', 'null', 'nan', '']).sum().sum()
            
            if valores_raros > 0:
                st.warning(f"⚠️ Se detectaron **{valores_raros}** valores de texto no válidos (ej: 'N/A', 'null' o celdas vacías con espacios).")

        #----------------------------------------------------------------------------------------------------------------------------------
        # LIMPIEZA Y CONVERSIÓN
        #----------------------------------------------------------------------------------------------------------------------------------
        
        #st.header("Panel de Limpieza")
        st.write("**Panel de Limpieza**")
        
        df_limpio          = st.session_state.data.copy()
        
        limpiar_duplicados = st.checkbox("Eliminar filas duplicadas")
        limpiar_nulos      = st.selectbox("¿Cómo manejar los valores nulos?", ["Mantenerlos", "Eliminar filas con nulos", "Reemplazar con la Media (Numéricas) / 'Desconocido' (Categóricas)"])
        forzar_fechas      = st.multiselect("Forzar conversión estricta a Fecha (datetime):", cat_cols)
    
        if st.button("Aplicar Limpieza y Conversiones"):
            
            for col in forzar_fechas:
                df_limpio[col] = pd.to_datetime(df_limpio[col], errors='coerce')
            
            if limpiar_duplicados:
                antes = len(df_limpio)
                df_limpio = df_limpio.drop_duplicates()
                st.success(f"✅ Se eliminaron {antes - len(df_limpio)} filas duplicadas.")
                
            if len(cat_cols) > 0:
                df_limpio[cat_cols] = df_limpio[cat_cols].replace([r'^\s*$', 'N/A', 'na', 'NaN', 'null'], np.nan, regex=True)
                
            if limpiar_nulos == "Eliminar filas con nulos":
                antes     = len(df_limpio)
                df_limpio = df_limpio.dropna()
                st.success(f"✅ Se eliminaron {antes - len(df_limpio)} filas que contenían valores nulos.")
                
            elif limpiar_nulos == "Reemplazar con la Media (Numéricas) / 'Desconocido' (Categóricas)":
                num_actuales = df_limpio.select_dtypes(include=[np.number]).columns
                cat_actuales = df_limpio.select_dtypes(include=['object', 'category']).columns
                
                for col in num_actuales:
                    df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mean())
                for col in cat_actuales:
                    df_limpio[col] = df_limpio[col].fillna("Desconocido")
                st.success("✅ Valores nulos reemplazados correctamente.")
                
            st.write("📋 **Dataset Limpio Resultante**")
            st.write(df_limpio.head())

        st.info("Diríjase al Módulo **Análisis Visual** para graficar el dataset.")
            
    else:
        st.warning(
            "🚨 Primero debe cargar un dataset.  \n"
            "Diríjase al Módulo **Carga y Perfil del Dataset**."
        )

###########################################################################################################################################
# MODULO: ANALISIS VISUAL
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

        #----------------------------------------------------------------------------------------------------------------------------------
        # Creación de Tabs
        #----------------------------------------------------------------------------------------------------------------------------------
        
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Resumen", 
                                                      "Análisis Univariado",
                                                      "Análisis Bivariado",
                                                      "Análisis Multivariado",
                                                      "Análisis Temporal",
                                                      "Insights"])

        #----------------------------------------------------------------------------------------------------------------------------------
        # Resumen
        #----------------------------------------------------------------------------------------------------------------------------------
        
        with tab1:
            
            st.header("Resumen")

            st.write("**Indicadores Principales**")

            # Cálculos matemáticos iniciales
            # Filas y Columnas
            filas, columnas    = data.shape
            # Cálculo de nulos globales
            nulos_totales      = data.isnull().sum().sum()
            # Cálculo de duplicados globales
            duplicados_totales = data.duplicated().sum()
            celdas_totales     = data.size
            porcentaje_nulos   = (nulos_totales / celdas_totales) * 100 if celdas_totales > 0 else 0

            # Renderizado en tarjetas de Streamlit (Métricas de lectura rápida)
            ind1, ind2, ind3, ind4 = st.columns(4)
            with ind1:
                st.metric("Total de Registros (Filas)", f"{filas:,}")
            with ind2:
                st.metric("Total de Variables (Columnas)", columnas)
            with ind3:
                # Métricas para Nulos
                st.metric("Valores Nulos (Celdas)", f"{nulos_totales:,}", 
                          delta=f"{porcentaje_nulos:.2f}% del total", delta_color="inverse")
            with ind4:
                # Métricas para Duplicados
                st.metric("Filas Duplicadas", f"{duplicados_totales:,}", 
                          delta="Acción requerida" if duplicados_totales > 0 else "Limpio", 
                          delta_color="inverse" if duplicados_totales > 0 else "normal")

            -- Imprime una línea en la pantalla
            st.markdown("---")
        
            st.write("**Tabla de Dimensiones**")

            df_dimensiones = pd.DataFrame({
                "Métrica de Estructura": ["Filas (Registros)", "Columnas (Variables)", "Total de Celdas Evaluadas"],
                "Cantidad": [filas, columnas, celdas_totales]
            })
            st.dataframe(df_dimensiones, hide_index=True, use_container_width=True)
            
            st.subheader("Visualizando los 10 Primeros Registros")
            st.dataframe(data.head(10), use_container_width=True)
        
            st.write("**Tipos de Datos**")
            st.write("**Nulos**")
            st.write("*Resumen Estadístico**")
            
        #----------------------------------------------------------------------------------------------------------------------------------
        # Análisis Univariado
        #----------------------------------------------------------------------------------------------------------------------------------
        
        with tab2:
            
            st.header("Análisis Univariado") 

            st.write("**Histogramas**")
            st.write("**Boxplots**")
            st.write("**Conteo de Categorías**")
            st.write("**Proporciones**")
            st.write("*Distribución de Variables Individuales**")

        #----------------------------------------------------------------------------------------------------------------------------------
        # Análisis Bivariado
        #----------------------------------------------------------------------------------------------------------------------------------

        with tab3:
            
            st.header("Análisis Bivariado")

            st.write("**Scatter Plots**")
            st.write("**Boxplots por Categoría**")
            st.write("**Barras Agrupadas**")
            st.write("**Comparación entre Variables Numéricas y Categóricas**")

        #----------------------------------------------------------------------------------------------------------------------------------
        # Análisis Multivariado
        #----------------------------------------------------------------------------------------------------------------------------------

        with tab4:
            st.header("Análisis Multivariado")

            st.write("**Correlación**")
            st.write("**Headmap**")
            st.write("**Tipos de Datos**")
            st.write("**Nulos**")
            st.write("*Resumen Estadístico**")

        #----------------------------------------------------------------------------------------------------------------------------------
        # Análisis Temporal
        #----------------------------------------------------------------------------------------------------------------------------------

        with tab5:
            
            st.header("Análisis Temporal")

        #----------------------------------------------------------------------------------------------------------------------------------
        # Temporal
        #----------------------------------------------------------------------------------------------------------------------------------
        
        with tab6:
            st.header("Insights")

        #----------------------------------------------------------------------------------------------------------------------------------
        # Final de Tabs
        #----------------------------------------------------------------------------------------------------------------------------------
    
    else:
        st.warning(
            "🚨 Primero debe cargar un dataset.  \n"
            "Diríjase al Módulo **Carga y Perfil del Dataset**."
        )

###########################################################################################################################################
# FIN DE CODIGO
###########################################################################################################################################
###########################################################################################################################################
