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
# 1. CONFIGURACIÓN
st.set_page_config(page_title="Master en Bucles - UTS", page_icon="💻", layout="wide")

st.title("🚀 Desafío de Ingeniería: Construcción de Bucles")
st.markdown("---")

# --- SECCIÓN DE RETO DE PROGRAMACIÓN ---
st.header("🎯 Reto: Programación de Tablas de Multiplicar")
st.write("""
**Instrucciones:** No basta con la fórmula. Debes escribir el ciclo completo en Python para generar la tabla.
Usa la variable `base` que te asigna el sistema.
""")

if 'base_reto' not in st.session_state:
    st.session_state.base_reto = random.randint(2, 9)

base = st.session_state.base_reto

col_input, col_output = st.columns([1.2, 0.8])

with col_input:
    st.info(f"👉 **RETO:** Generar la tabla del **{base}** (del 1 al 10)")
    
    # Área de texto para código multilínea
    codigo_usuario = st.text_area(
        "Escribe tu código Python aquí:",
        value=f"# Ejemplo:\nfor i in range(1, 11):\n    print(base * i)",
        height=150
    )
    
    if st.button("🎲 Cambiar Número"):
        st.session_state.base_reto = random.randint(2, 9)
        st.rerun()

with col_output:
    st.subheader("🖥️ Ejecución y Validación")
    
    if codigo_usuario:
        # Capturamos la salida del print()
        f = io.StringIO()
        try:
            with contextlib.redirect_stdout(f):
                # Ejecutamos el código del alumno en un entorno controlado
                # Pasamos 'base' como variable global disponible
                exec(codigo_usuario, {"base": base, "print": print})
            
            # Obtenemos lo que el alumno imprimió
            salida = f.getvalue().strip().split('\n')
            
            # Limpiamos y convertimos a números para validar
            resultados_alumno = []
            for val in salida:
                try:
                    # Intentamos extraer el último número de la línea o la línea completa
                    num = int(val.split('=')[-1].strip())
                    resultados_alumno.append(num)
                except:
                    continue

            # VALIDACIÓN LÓGICA
            esperado = [base * i for i in range(1, 11)]
            
            if resultados_alumno == esperado:
                st.balloons()
                st.success("✨ ¡CÓDIGO PERFECTO! Has construido el ciclo correctamente.")
                st.write("**Tu salida:**")
                st.code(f.getvalue())
            else:
                st.error("❌ La salida no coincide con la tabla esperada.")
                st.write("**Tu salida actual:**")
                st.code(f.getvalue() if f.getvalue() else "No hubo salida (usa print)")
                st.info(f"Pista: Tu código debe imprimir exactamente 10 valores: {esperado}")

        except Exception as e:
            st.warning(f"⚠️ Error de sintaxis en tu código: {e}")

st.divider()

# --- SECCIÓN VISUAL DE COMPARACIÓN ---
st.subheader("💡 Ayuda Visual: Estructura de los Ciclos")
col_for, col_while = st.columns(2)

with col_for:
    st.markdown("**Patrón del Ciclo FOR**")
    st.code(f"for i in range(1, 11):\n    resultado = {base} * i\n    print(resultado)", language="python")
    st.caption("Ideal cuando conoces el número exacto de vueltas.")

with col_while:
    st.markdown("**Patrón del Ciclo WHILE**")
    st.code(f"i = 1\nwhile i <= 10:\n    print({base} * i)\n    i += 1", language="python")
    st.caption("Ideal cuando dependes de una condición lógica.")

st.caption("Laboratorio de Programación UTS - Ing. Nelber Montaguth")
