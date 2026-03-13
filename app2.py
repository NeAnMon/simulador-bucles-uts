import streamlit as st
import time
import pandas as pd
import random
import io          # IMPORTANTE: Añadido
import contextlib  # IMPORTANTE: Añadido

# 1. CONFIGURACIÓN ÚNICA (Debe ser la primera de Streamlit)
st.set_page_config(page_title="Master en Bucles - UTS", page_icon="💻", layout="wide")

# Estilo Profesional
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
    st.caption("Prueba: `i**2` (potencia), `7 * (i+1)` (tabla)")

with col4:
    try:
        resultados_libres = [{"Iteración": i, "Resultado": eval(formula, {"i": i})} for i in range(rango_lab)]
        st.dataframe(pd.DataFrame(resultados_libres), use_container_width=True)
    except:
        st.error("Error en la fórmula. Asegúrate de usar la variable 'i'.")

st.divider()

# ==========================================
# 4. SECCIÓN 3: RETO DE PROGRAMACIÓN (CON EXEC)
# ==========================================

st.header("🎯 Reto de Programación: Tablas de Multiplicar")
st.write("Demuestra tu lógica de programación. Debes construir el ciclo completo.")

if 'base_reto' not in st.session_state:
    st.session_state.base_reto = random.randint(2, 9)

base = st.session_state.base_reto
col_input, col_output = st.columns([1, 1])

with col_input:
    st.info(f"👉 **TU MISIÓN:** Generar la tabla del **{base}** (del 1 al 10)")
    
    # El área de código ahora está vacía para forzarlos a pensar
    codigo_usuario = st.text_area(
        "Escribe tu código Python aquí:",
        placeholder="# Pista: Usa un ciclo for o while y la variable 'base'\n# No olvides el print()",
        height=200
    )
    
    # PISTA SENCILLA (Sustituye a la ayuda visual anterior)
    with st.expander("💡 ¿Necesitas una pista?"):
        st.write("""
        **Recuerda la estructura básica:**
        1.  Inicia el ciclo (usa `for` con `range` o un `while` con un contador).
        2.  Calcula el resultado usando la variable `base`.
        3.  Muestra el resultado con `print()`.
        4.  *Si usas while, ¡no olvides aumentar el contador!*
        """)

    if st.button("🎲 Generar otro número"):
        st.session_state.base_reto = random.randint(2, 9)
        st.rerun()

with col_output:
    st.subheader("🖥️ Validador de Algoritmo")
    if codigo_usuario:
        f = io.StringIO()
        try:
            with contextlib.redirect_stdout(f):
                # Ejecutamos con acceso a 'base'
                exec(codigo_usuario, {"base": base, "print": print})
            
            salida = f.getvalue().strip().split('\n')
            resultados_alumno = []
            for val in salida:
                try:
                    # Extraer el último número de la línea
                    num = int(val.split('=')[-1].strip())
                    resultados_alumno.append(num)
                except:
                    continue

            # Validación contra el resultado esperado
            esperado = [base * i for i in range(1, 11)]
            
            if resultados_alumno == esperado:
                st.balloons()
                st.success("✨ ¡EXCELENTE! Algoritmo validado con éxito.")
                st.code(f.getvalue(), language="text")
            else:
                st.error("❌ El resultado no es el esperado.")
                if not f.getvalue():
                    st.warning("Tu código no imprimió nada. Usa print() para mostrar los resultados.")
                else:
                    st.write("Tu código imprimió:")
                    st.code(f.getvalue(), language="text")

        except Exception as e:
            st.error(f"⚠️ Error de sintaxis o lógica: {e}")

st.caption("Ingeniería de Sistemas UTS | Evaluación de Competencias Lógicas")
