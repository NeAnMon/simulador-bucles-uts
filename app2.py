import streamlit as st
import time
import pandas as pd

# Configuración de Entorno de Ingeniería
st.set_page_config(page_title="Algoritmos Avanzados - UTS", page_icon="💻", layout="wide")

st.title("🚀 Laboratorio de Algoritmos: Bucles y Procesamiento de Datos")
st.markdown("""
En este nivel, no basta con ver el ciclo; debes **construir la lógica**. 
Aprenderás a usar acumuladores, contadores y validadores dentro de estructuras repetitivas.
""")

# --- SECCIÓN 1: EL DESAFÍO DEL ACUMULADOR ---
st.header("1. El Desafío del Acumulador (Sumatoria de Notas)")
st.write("Imagina que debes promediar las notas de un grupo de estudiantes de las UTS.")

col1, col2 = st.columns([1, 1])

with col1:
    num_notas = st.number_input("¿Cuántas notas vas a procesar?", 1, 10, 3)
    valor_nota = st.slider("Valor de cada nota (Simulación):", 0.0, 5.0, 3.5, step=0.1)
    
    st.markdown("### 🛠️ Completa el Algoritmo")
    st.write("Si el código fuera este, ¿qué valor debería tener el acumulador al final?")
    st.code(f"""
suma_total = 0
for i in range({num_notas}):
    nota = {valor_nota}
    suma_total = suma_total + nota
promedio = suma_total / {num_notas}
    """, language="python")

if st.button("▶️ Ejecutar Prueba de Escritorio"):
    col_a, col_b = st.columns(2)
    suma_temp = 0
    trazabilidad = []
    
    for i in range(num_notas):
        suma_temp += valor_nota
        trazabilidad.append({
            "Iteración": i + 1,
            "Valor Nota": valor_nota,
            "Suma Acumulada": round(suma_temp, 2),
            "Lógica": f"{round(suma_temp - valor_nota, 2)} + {valor_nota}"
        })
        
    with col_a:
        st.table(pd.DataFrame(trazabilidad))
    with col_b:
        promedio_final = suma_temp / num_notas
        st.metric("Promedio Final Calculado", round(promedio_final, 2))
        if promedio_final >= 3.0:
            st.success("Resultado: EL GRUPO APRUEBA")
        else:
            st.error("Resultado: EL GRUPO REPRUEBA")

st.divider()

# --- SECCIÓN 2: CONSOLA DE CÓDIGO INTERACTIVA (ADVANCED) ---
st.header("2. Consola Interactiva: Manipulación de Índices")
st.write("Aquí los estudiantes deben escribir la expresión que controla la **salida** del bucle.")

c3, c4 = st.columns([1, 1])

with c3:
    st.markdown("**Reto de Lógica:**")
    st.write("Genera una secuencia donde el valor se multiplique por el índice y se le sume una constante.")
    
    expresion = st.text_input("Ingresa tu expresión (ej: (i * 2) + 5):", "i * 10")
    repeticiones = st.slider("Número de ciclos:", 1, 20, 5)

with c4:
    st.markdown("**Depuración en Tiempo Real:**")
    try:
        resultados = []
        for i in range(repeticiones):
            # Seguridad: Evaluamos la expresión del alumno
            res = eval(expresion, {"i": i})
            resultados.append({"Índice (i)": i, "Tu Expresión": expresion, "Resultado": res})
        
        st.dataframe(resultados, use_container_width=True)
        
        # Gráfico de comportamiento lógico
        df_grafica = pd.DataFrame(resultados)
        st.line_chart(df_grafica["Resultado"])
        
    except Exception as e:
        st.warning("⚠️ Error en la sintaxis. Recuerda usar 'i' como tu variable de control.")

st.divider()

# --- SECCIÓN 3: ÁREA DE PROYECTO (MÉTODO DE CASOS) ---
with st.expander("📝 PROYECTO: Algoritmo de Control de Inventario Nexan"):
    st.write("""
    **Contexto:** En tu empresa **Nexan Soluciones Tecnológicas**, recibes un lote de 10 computadores. 
    Debes crear un ciclo que reste 1 al stock cada vez que se realice una venta, hasta que el stock llegue a cero.
    """)
    
    st.markdown("""
    **Preguntas de Ingeniería:**
    1. ¿Qué tipo de ciclo es más eficiente si no sabemos cuántas ventas se harán por hora? (`While` o `For`)
    2. ¿Cuál sería la **condición de parada** para evitar que el stock sea negativo?
    3. Escribe en la consola de arriba la expresión `10 - i` y observa el gráfico. ¿En qué iteración el stock llega a 5?
    """)

st.caption("Recurso de Nivel Avanzado para Ingeniería de Sistemas | UTS")
