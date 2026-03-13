import streamlit as st
import time
import pandas as pd
import random

# ==========================================
# 1. CONFIGURACIÓN Y ESTILO PROFESIONAL
# ==========================================
st.set_page_config(page_title="Lab Avanzado de Bucles - UTS", page_icon="🔁", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stTextInput>div>div>input { font-family: 'Courier New', monospace; color: #1A5276; }
    .stMetric { background-color: #ffffff; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔁 Laboratorio Avanzado de Bucles e Iteraciones")
st.markdown("---")

# ==========================================
# 2. SECCIÓN 1: VISUALIZADOR DE TRAZABILIDAD
# ==========================================
st.header("1. Visualizador de Trazabilidad (Paso a Paso)")
col1, col2 = st.columns([1, 2])

with col1:
    tipo = st.selectbox("Tipo de bucle:", ["Ciclo FOR (Rango)", "Ciclo WHILE (Condición)"])
    limite = st.slider("Número de iteraciones:", 1, 15, 5)
    velocidad = st.select_slider("Velocidad:", options=["Lento", "Normal", "Rápido"], value="Normal")
    delay = {"Lento": 1.0, "Normal": 0.5, "Rápido": 0.1}[velocidad]
    run_btn = st.button("🚀 Ejecutar y Rastrear")

with col2:
    if "FOR" in tipo:
        codigo_visual = f"for i in range({limite}):\n    print(f'Iteración: {{i}}')"
    else:
        codigo_visual = f"i = 0\nwhile i < {limite}:\n    print(f'Iteración: {{i}}')\n    i += 1"
    st.code(codigo_visual, language="python")

if run_btn:
    status = st.empty()
    progreso = st.progress(0)
    tabla_placeholder = st.empty()
    datos_iteracion = []
    
    for i in range(limite):
        status.markdown(f"**Ejecutando vuelta:** `{i + 1}` | **Valor de i:** `{i}`")
        progreso.progress((i + 1) / limite)
        datos_iteracion.append({"Vuelta": i + 1, "Valor de i": i, "Estado": "Completado"})
        tabla_placeholder.table(pd.DataFrame(datos_iteracion))
        time.sleep(delay)
    status.success(f"✅ ¡Ciclo completado con éxito!")

st.divider()

# ==========================================
# 3. SECCIÓN 2: LABORATORIO DE PRÁCTICA LIBRE
# ==========================================
st.header("2. Laboratorio de Código: Escribe tu Lógica")
col3, col4 = st.columns([1, 1])

with col3:
    formula = st.text_input("Ingresa tu operación matemática (usa 'i'):", "i * 10")
    rango_lab = st.number_input("¿Cuántas repeticiones?", 1, 50, 5)
    st.caption("Prueba: `i**2` (potencia), `7 * (i+1)` (tabla), `100 - (i*5)` (descenso)")

with col4:
    try:
        resultados_libres = [{"Iteración": i, "Resultado": eval(formula, {"i": i})} for i in range(rango_lab)]
        st.dataframe(pd.DataFrame(resultados_libres), use_container_width=True)
    except:
        st.error("Error en la fórmula. Asegúrate de usar la variable 'i'.")

st.divider()

# ==========================================
# 4. SECCIÓN 3: DESAFÍO DE CERTIFICACIÓN (TABLAS)
# ==========================================
st.header("🎯 Desafío Pro: El Validador de Tablas")
st.write("Demuestra tu dominio de los patrones. Debes programar la lógica para la tabla que el sistema te asigne.")

# Persistencia del número base en la sesión
if 'base_reto' not in st.session_state:
    st.session_state.base_reto = random.randint(2, 9)

base = st.session_state.base_reto
col_input, col_valid = st.columns([1, 1])

with col_input:
    st.info(f"👉 **RETO:** Programar la tabla del **{base}**")
    codigo_estudiante = st.text_input("Escribe la expresión para calcular el resultado (usa 'i'):", placeholder="Ej: i * base")
    
    if st.button("🎲 Cambiar Número de Tabla"):
        st.session_state.base_reto = random.randint(2, 9)
        st.rerun()

with col_valid:
    if codigo_estudiante:
        try:
            fallos = 0
            check_data = []
            for i in range(10):
                esperado = base * (i + 1)
                intento = eval(codigo_estudiante, {"i": i, "base": base})
                es_valido = (intento == esperado)
                if not es_valido: fallos += 1
                check_data.append({"Multiplicación": f"{base} x {i+1}", "Tu Valor": intento, "Correcto": esperado, "Status": "✅" if es_valido else "❌"})
            
            st.dataframe(pd.DataFrame(check_data), use_container_width=True)
            
            if fallos == 0:
                st.balloons()
                st.success(f"¡LOGRADO! Tu algoritmo para la tabla del {base} es perfecto.")
            else:
                st.error(f"Lógica incorrecta: fallaste en {fallos} resultados. ¡Ajusta tu fórmula!")
        except Exception as e:
            st.warning("⚠️ Error de sintaxis. Revisa el uso de operadores como `*`.")

st.divider()
st.caption("Ingeniería de Sistemas - UTS | Desarrollado por el Ing. Nelber Montaguth")
