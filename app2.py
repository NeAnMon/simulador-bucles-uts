import streamlit as st
import time
import pandas as pd

# Configuración técnica
st.set_page_config(page_title="Laboratorio Avanzado de Bucles - UTS", page_icon="🔁", layout="wide")

st.title("🔁 Laboratorio Avanzado de Bucles e Iteraciones")
st.markdown("""
Bienvenido al entorno de experimentación de ciclos. Aquí podrás visualizar cómo la computadora 
procesa patrones repetitivos y probar tu propio código.
""")

# --- SECCIÓN 1: VISUALIZADOR DE TRAZABILIDAD ---
st.header("1. Visualizador de Trazabilidad (Paso a Paso)")
st.info("Configura el ciclo y observa cómo cambian las variables en cada 'vuelta'.")

col1, col2 = st.columns([1, 2])

with col1:
    tipo = st.selectbox("Selecciona el tipo de bucle:", ["Ciclo FOR (Rango)", "Ciclo WHILE (Condición)"])
    limite = st.slider("Número de iteraciones:", 1, 15, 5)
    velocidad = st.select_slider("Velocidad de ejecución:", options=["Lento", "Normal", "Rápido"], value="Normal")
    
    delay = {"Lento": 1.0, "Normal": 0.5, "Rápido": 0.1}[velocidad]
    run_btn = st.button("🚀 Ejecutar y Rastrear")

with col2:
    st.write("**Código equivalente en Python:**")
    if "FOR" in tipo:
        codigo_visual = f"for i in range({limite}):\n    # En cada vuelta i aumenta automáticamente\n    print(f'Iteración: {{i}}')"
    else:
        codigo_visual = f"i = 0\nwhile i < {limite}:\n    # Debemos aumentar i manualmente\n    print(f'Iteración: {{i}}')\n    i += 1"
    st.code(codigo_visual, language="python")

if run_btn:
    # Contenedores para la visualización dinámica
    status = st.empty()
    progreso = st.progress(0)
    tabla_placeholder = st.empty()
    
    datos_iteracion = []
    
    for i in range(limite):
        # Actualizar estado
        status.markdown(f"**Ejecutando vuelta:** `{i + 1}` de `{limite}` | **Valor de i:** `{i}`")
        progreso.progress((i + 1) / limite)
        
        # Guardar datos para la tabla de trazabilidad
        datos_iteracion.append({"Vuelta": i + 1, "Valor de i": i, "Estado": "Procesando..."})
        df = pd.DataFrame(datos_iteracion)
        tabla_placeholder.table(df)
        
        time.sleep(delay)
    
    status.success(f"✅ ¡Ciclo completado! Se realizaron {limite} iteraciones exitosas.")

st.divider()

# --- SECCIÓN 2: LABORATORIO DE EXPERIMENTACIÓN LIBRE ---
st.header("2. Laboratorio de Código: Escribe tu Lógica")
st.write("Usa la variable `i` para crear una secuencia. La computadora calculará el resultado en cada paso.")

col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("**Configura tu lógica personalizada:**")
    formula = st.text_input("Ingresa una operación matemática (ej: 5 * i o i**2):", "10 * i")
    rango_lab = st.number_input("¿Cuántas veces quieres repetir?", 1, 50, 5)
    
    st.markdown("""
    **Sugerencias para probar:**
    * Tablas de multiplicar: `7 * (i + 1)`
    * Potencias: `2 ** i`
    * Sucesiones: `100 - (i * 5)`
    """)

with col4:
    st.markdown("**Resultado de la Consola:**")
    resultados_finales = []
    try:
        for i in range(rango_lab):
            valor_calculado = eval(formula, {"i": i})
            resultados_finales.append({"Iteración": i, "Fórmula": formula.replace("i", str(i)), "Resultado": valor_calculado})
        
        st.dataframe(resultados_finales, use_container_width=True)
    except Exception as e:
        st.error(f"Error en la lógica: Verifica que estés usando la variable 'i' correctamente.")

st.divider()

# --- SECCIÓN 3: EL RETO DEL BUCLE INFINITO ---
with st.expander("🚩 RETO AVANZADO: Identificación de Patrones"):
    st.markdown("""
    **Misión:** Quieres crear un programa que cuente del **10 al 100 de diez en diez**.
    
    1. En el **Laboratorio**, ¿qué fórmula escribirías para que cuando `i=0` el resultado sea 10, y cuando `i=1` sea 20?
    2. ¿Cuántas repeticiones necesitas para llegar al 100?
    
    *Pista: La lógica tiene la forma `(i + 1) * X`. Encuentra el valor de X.*
    """)

st.caption("Recurso de Ingeniería de Sistemas - Unidades Tecnológicas de Santander")
